#!/usr/bin/env python3
# Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>
# 'Time-stamp: <2020/08/26 13:15:19 fuyuki lexer.py>'

import sys
import pprint as ppr
import collections.abc
import json
import string
import getopt
import os.path
import itertools

import pyparsing as pp
# pp.ParserElement.enablePackrat()   # does not help, even worse


class FileTree:
    """File tree for LaTeX document."""

    def __init__(self, file, parent=None):
        """Store FILE binding to LEX."""
        if isinstance(file, str):
            self.file = file
        else:
            self.file = file.name

        self.parent = parent
        self.children = []
        self.lex = None
        if parent:
            self.root = parent.root
        else:
            self.root = self

    def add(self, file):
        """Add child."""
        ch = FileTree(file, self)
        self.children.append(ch)
        return(ch)

    def aslist(self):
        """Return file tree as list."""
        if self.children:
            return({self.file: [ch.aslist() for ch in self.children]})
        else:
            return({self.file: None})

    def walk(self):
        """Iterate through tree."""
        yield self
        for ch in self.children or []:
            yield from ch.walk()


class LexerBase:
    """Core lexer/parser class for LaTeX document."""

    def __init__(self,
                 macros=None, envs=None,
                 arrays=None,
                 atletter=False,
                 verbose=None,
                 debug=False, *args, **kw):
        """Initialize pyparsing definition."""
        default_whites = pp.ParserElement.DEFAULT_WHITE_CHARS
        pp.ParserElement.setDefaultWhitespaceChars('')

        self.verbose = verbose or 0

        self.ftree = None
        macros = macros or {}
        envs = envs or {}
        arrays = arrays or {}
        self.debug = debug
        self.report = {}

        self.cache = {}

        self.pe_macros = {}           # ParserElement of macros
        self.pe_envs = {}           # ParserElement of environments

        uc_whites = [chr(12288)]
        # 12288: 2 byte white space [　]
        uc_puncts = []

        esc = '\\'              # catcode 0
        lbr = r'{'              # catcode 1
        rbr = r'}'              # catcode 2
        com = r'%'              # catcode 14
        mxp = r'$'              # catcode 3

        amp = r'&'              # catcode 4
        lbs = r'['
        rbs = r']'
        par = r'#'              # catcode 6

        excl = [com, esc, lbr, rbr, mxp, amp, lbs, rbs, par]

        # (a part of) TeX special charcters % \ { } $ #&~_^

        self.com = pp.Literal(com)
        self.esc = pp.Literal(esc)
        self.lbr = pp.Literal(lbr)
        self.rbr = pp.Literal(rbr)
        self.mxp = pp.Literal(mxp)

        # symbols
        self.amp = pp.Literal(amp)
        self.par = pp.Literal(par)
        self.lbs = pp.Literal(lbs)
        self.rbs = pp.Literal(rbs)

        # single-char symbols
        self.ssym = pp.MatchFirst([self.amp, self.lbs, self.rbs])

        # nl
        self.nl = pp.LineEnd()
        # ws
        self.ws = pp.White()
        # comment line
        self.cline = pp.Combine(self.com + pp.restOfLine() + self.nl)
        # self.cline = cline.setResultsName('%')

        # letters
        self.letters = pp.Forward()
        # cseq
        self.cseq = pp.Combine(self.esc + self.letters)

        self.atletter = pp.Combine(self.esc
                                   + pp.Literal('makeatletter'))
        self.atother = pp.Combine(self.esc
                                  + pp.Literal('makeatother'))

        # letters (catcode 11)
        def action_atletter(toks):
            r"""Emulate \makeatletter."""
            self.letters << pp.Word(pp.alphas + r'@')

        def action_atother(toks):
            r"""Emulate \makeatother."""
            self.letters << pp.Word(pp.alphas)

        self.atletter.setParseAction(action_atletter)
        self.atother.setParseAction(action_atother)

        # positional parameters
        self.posp = pp.Combine(pp.OneOrMore(self.par) + pp.Char('123456789'))

        # escaped symbols
        self.cr = pp.Literal(esc + esc)
        # string.punctuation
        self.esym = pp.MatchFirst([pp.Combine(pp.Literal(esc + ch))
                                   for ch in string.punctuation + ' '
                                   if ch not in [lbs, rbs, esc]])

        self.usym = pp.MatchFirst([pp.Combine(pp.Literal(esc + ch))
                                   for ch in uc_puncts])

        # special whitespace
        self.uws = pp.oneOf(uc_whites)

        # normal
        xch = ''.join(excl)
        self.atext = pp.Combine(pp.Word(pp.printables + ' ',
                                        excludeChars=xch)
                                + pp.Optional('\n'))

        self.utext = pp.CharsNotIn(pp.printables
                                   + '\n\t ' + ''.join(uc_whites))
        self.normal = (self.atext | self.utext)

        # recursive elements
        self.group = pp.Forward()
        self.opt = pp.Forward()
        self.imath = pp.Forward()
        self.xmath = pp.Forward()
        self.dmath = pp.Forward()
        self.envgroup = pp.Forward()

        # whitespaces or empty
        self.blanks = pp.Combine(pp.OneOrMore(self.cline | self.ws | self.nl)
                                 | pp.Empty())

        # single \begin \end
        single_begin = self.lex_begin()
        single_begin.setParseAction(self.action_unmatched)
        self.benv = pp.Group(single_begin)

        single_end = self.lex_end()
        single_end.setParseAction(self.action_unmatched)
        self.eenv = pp.Group(single_end)

        # \verb
        verb_sep = (pp.Char(string.punctuation)
                    | pp.Literal(' ') | pp.Literal('\n'))
        verb_head = (pp.Combine(self.esc + pp.Literal(r'verb')('M'))
                     + verb_sep('L'))
        verb_foot = pp.Forward()

        def action_endverb(toks):
            r"""Emulate \verb."""
            right = pp.Literal(toks.L)
            e = (right | pp.StringEnd())
            ee = (right('R') | pp.StringEnd())
            c = pp.SkipTo(e)
            verb_foot << pp.Combine(c('C') + ee)

        verb_head.setParseAction(action_endverb)
        vlex = verb_head + verb_foot

        def adj_verb(s, loc, toks):
            r"""Adjust verbatim string."""
            if 'R' in toks:
                toks[-1] = toks[-1][:-1]
                toks.append(toks.R)
                toks['A'] = [toks.L, toks.C, toks.R]
            else:
                self.append_report('unclosed', s, loc, toks)
            return(toks)

        vlex.setParseAction(adj_verb)

        # todo  <\verb  >  cannot be handled  (i.e., \verb SPACE null SPACE)
        vsp2 = pp.Literal(r'\verb  ') | pp.Literal(r'\verb\n\n')
        vnl2 = pp.Combine(pp.Literal(r'\verb') + pp.LineEnd() + pp.LineEnd())

        # need to encapsulate
        self.verb = pp.Group(vsp2('T') | vnl2('T') | vlex('T'))

        # def
        self.defs = self.lex_def([r'def', r'gdef', r'xdef', r'edef'])

        # macros (on-the-fly)
        self.motf = pp.Forward()

        # macros
        self.pe_macros = {'makeatletter': self.atletter,
                          'makeatother': self.atother,
                          'def': self.defs}

        for m, a in macros.items():
            self.pe_macros[m] = self.lex_macro(m, a)

        self.mlex = pp.MatchFirst([pp.Group(e)
                                   for e in self.pe_macros.values()])

        # caution
        # set_parse_action failed if pe_envs is [pp.Group(envgroup)]
        # Due to unknown reason, pe_envs must be [envgroup]

        self.cenv = [True]
        # array type environments
        eall = []
        for e, a in arrays.items():
            lp = self.lex_env_group(e, a, True)
            self.pe_envs[e] = lp
            # lp.setParseAction(self.action_dummy)
            eall.append(lp)

        # environments
        for e, a in itertools.chain(envs.items(), [(None, None)]):
            lp = self.lex_env_group(e, a)
            self.pe_envs[e] = lp
            eall.append(lp)

        self.elex = pp.MatchFirst([pp.Group(e)
                                   for e in self.pe_envs.values()])

        # fallback
        self.fallback = pp.Combine(self.esc + pp.Regex('.')) | pp.Regex('.')
        self.fallback.setParseAction(self.action_fallback)

        # expr
        contents = (self.normal
                    | self.motf
                    | self.mlex
                    | self.verb
                    | self.elex
                    | self.benv | self.eenv
                    | self.cseq | self.cr | self.esym | self.ssym
                    | self.xmath | self.imath | self.dmath
                    | self.group
                    | self.nl | self.ws
                    | self.posp
                    | self.uws | self.usym)
        # if self.debug:
        #     contents.setDebug()
        skip = (self.cline)
        fb = (self.fallback)

        self.expr = (contents.setResultsName('N', True)
                     | skip.setResultsName('%', True)
                     | fb.setResultsName('N', True))

        # # column
        # cr = pp.Literal(esc + esc)
        # sep = cr | self.amp
        # self.column = (sep | pp.Group(pp.ZeroOrMore(~sep + self.expr)))

        # group { }
        self.group << self.gen_group(self.lbr, self.rbr)
        # opt [ ]
        self.opt << self.gen_group(self.lbs, self.rbs)
        # inline math $ $
        self.imath << self.gen_group(self.mxp)
        # display math $$ $$
        self.dmx = pp.Literal(mxp + mxp)
        self.xmath << self.gen_group(self.dmx)
        # display math \[ \]
        self.ldm = pp.Literal(esc + lbs)
        self.rdm = pp.Literal(esc + rbs)

        self.dmath << self.gen_group(self.ldm, self.rdm)

        # Important: self.letters must be defined after defs
        if atletter:
            action_atletter(None)
        else:
            action_atother(None)

        # core lexer
        self.lex = (pp.ZeroOrMore(~pp.StringEnd() + self.expr))

        # some adjustment for debug
        for k in dir(self):
            lp = getattr(self, k)
            if isinstance(lp, pp.ParserElement):
                lp.setName(k.upper())
                if self.debug:
                    lp.setDebug()

        #
        pp.ParserElement.setDefaultWhitespaceChars(default_whites)
        return

    def gen_group(self, left, right=None, c=None, pfx=None):
        """Generate grouped token wtih LEFT RIGHT delimiters."""
        right = right or left
        if c is None:
            c = pp.ZeroOrMore(~right + self.expr)
            c = c.setResultsName('C')
        g = (left('L') + c + (right('R') | pp.StringEnd()))
        g.setParseAction(self.action_group)
        g = g.setResultsName('A')
        if pfx:
            g = pfx + g
        return(pp.Group(g))

    def action_fallback(self, s, loc, toks):
        """Remember fallback token."""
        self.append_report('fallback', s, loc, toks)

        return

    def action_group(self, s, loc, toks):
        """Check if closed."""
        if 'R' in toks:
            pass
        else:
            self.append_report('unclosed', s, loc, toks)
        return

    def action_unmatched(self, s, loc, toks):
        """Remember unmatched token."""
        # t = self.unparse(toks.T)
        self.append_report('unmatched', s, loc, toks)
        return

    def lex_def(self, macro=None, args=None):
        r"""Define lexer for \def\macro...{content}."""
        macro = macro or r'def'
        if isinstance(macro, str):
            macro = pp.Literal(macro)
        elif self.is_iterable(macro):
            macro = pp.MatchFirst([pp.Literal(j) for j in macro])

        args = args or 1

        cs = pp.Combine(self.esc + macro)
        name = pp.Combine(self.esc + self.letters)
        pl = [pp.Combine(self.par + pp.Literal('%d' % j))
              for j in range(1, 10)]
        sep = pp.SkipTo((self.lbr | self.par))
        par = pp.Optional(pl[-1] + sep)
        for j in reversed(pl[:-1]):
            par = pp.Optional(j + sep + par)
        ptm = pp.Combine(self.par + pp.FollowedBy(self.lbr))
        lex = (cs + name
               + pp.Group(sep + pp.Optional(par) + pp.Optional(ptm)))
        alex = self.gen_aset(args)
        if alex:
            lex = lex + alex
        return(lex)

    def lex_env_group(self, name, args=None, array=False):
        r"""Define lexer for tex typical \begin{ENV} with arguments.

        ARGS: a number or list to control the argument list.
           NARG or [NARG, INDEX, ....]
           NARG:  total number of arguments
           INDEX:  index of optional argument (start from 1)
        examples
           \begin{ENV}                 args=None  (or 0)
           \begin{ENV}{A}{B}           args=2
           \begin{ENV}[ ][ ]           args=[2, 1, 2]
           \begin{ENV}[ ]{A}{B}        args=[3, 1]
           \begin{ENV}[ ]{A}{B}[ ]{C}  args=[5, 1, 4]

        Todo:
              ungrouped arguments are not treated.

        """
        envgroup = pp.Forward()

        open_env = self.lex_begin(name, args)
        open_env.setName('BEGIN')
        if self.debug:
            open_env.setDebug()
        close_env = pp.Forward()

        def gen_close(toks):
            """Close environemnt."""
            # print(repr(toks.E.C))
            env = toks.E.C
            end = self.lex_end(env)
            if array:
                # todo: grouping by lines
                sep = self.cr | self.amp
                # item = pp.Group(pp.ZeroOrMore(~sep + ~end + self.expr)
                #                 + pp.Optional(sep('S')))
                # item = item.setResultsName('I', True)
                col = pp.Group(pp.ZeroOrMore(~sep + ~end + self.expr)
                               + pp.Optional(self.amp('S')))
                line = (pp.ZeroOrMore(~self.cr + ~end
                                      + col.setResultsName('I', True))
                        + pp.Optional(self.cr('R')))
                line.setParseAction(self.action_array_row)
                item = pp.Group(line)
            else:
                # need to separate self.cr
                # otherwise CR is not detected  (strange...)
                item = self.cr | self.expr
            body = pp.ZeroOrMore(~end + item)
            close_env << (body.setResultsName('B')
                          + pp.Group(end).setResultsName('Z'))
            return

        open_env.setParseAction(gen_close)
        open_env.addParseAction(self.tree_env_push)

        # envgroup << pp.Group(open_env + close_env)
        envgroup << open_env + close_env
        if self.debug:
            envgroup.setDebug()
        if name:
            name = 'ENV/%s' % name
        else:
            name = 'ENV'
        envgroup.setName(name)
        envgroup.setParseAction(self.tree_env_pop)
        return(envgroup)

    def tree_env_push(self, s, loc, toks):
        """Generate environment tree."""
        self.cenv.append(toks.E.C)
        return(None)

    def tree_env_pop(self, s, loc, toks):
        """Generate environment tree."""
        self.cenv.pop(-1)
        return(None)

    def lex_begin(self, name=None, args=None, macro=None):
        r"""Define lexer for \begin{NAME} starter."""
        if name is None:
            name = pp.Word(pp.alphas + '*')
        elif isinstance(name, str):
            name = pp.Literal(name)
        earg = self.gen_group(self.lbr, self.rbr,
                              name('C'), pfx=pp.Optional(self.blanks))
        earg = earg('E')

        macro = macro or r'begin'
        lex = self.lex_macro(macro, args, ins=earg)

        return(lex)

    def lex_end(self, name=None):
        r"""Define lexer for \end{NAME}."""
        lex = self.lex_begin(name, macro=r'end')
        return(lex)

    def lex_macro(self, macro, args=None, ins=None):
        r"""Define lexer for tex typical macro with arguments.

        Todo: * is not treated.
              ungrouped arguments are not treated.
        INS is insert after \MACRO (e.g, used for \begin{ENV})

        """
        name = pp.Literal(macro)('M') + ~self.letters
        cs = pp.Combine(self.esc + name)

        alex = self.gen_aset(args)

        lex = cs
        if ins:
            lex = lex + ins
        if alex:
            lex = lex + pp.Group(alex).setResultsName('P')
        # if alex:
        #     alex = pp.Group(alex)
        # else:
        #     alex = pp.Group(pp.Empty())
        # lex = lex + alex.setResultsName('P')

        lex.setName('MACRO/%s' % macro)
        # 'MACRO', [[ARG], [ARG], ...]
        return(lex('T'))

    def gen_aset(self, args=None):
        """Generate option/parameter list."""
        # Todo: optional arguments if not separated by blank
        # Todo: xparse type arguments list
        # (e.g., frame in beamer class)
        # True: {mandatory}   False: [optional]
        args = args or 0
        if args == 0:
            return None
        if isinstance(args, int):
            args = [args]
        if args[0] == 0:
            return None

        # None is sentry (start=1)
        aset = [None] + [True] * args[0]
        for a in args[1:]:
            aset[a] = False

        alex = []
        for j, a in enumerate(aset[1:], start=1):
            n = '#%d' % j
            if a:
                e = self.group
            else:
                e = pp.Optional(self.opt)
            ap = pp.Optional(self.blanks) + e(n)
            alex.append(ap)
        alex = pp.And(alex)

        return(alex)

    def action_section(self, s, loc, toks):
        """Update section."""
        k = 'sec'
        m = toks.M
        j = self.sects.index(m)
        c = self.counters[k]
        if isinstance(c, int):
            c = (c, )
        if len(c) <= j:
            c = c + (0, ) * (j - len(c)) + (1, )
        else:
            c = c[:j] + (c[j] + 1, )
        self.counters[k] = c
        return(None)

    def search(self, tree=None, *macros):
        """Search all the MACROS occurence in TREE.

        Macro in MACROS must be defined in LexerBase if with arguments.
        Only registered macros can be searched.
        """
        tree = tree or self.ftree.lex
        r = []
        for t in tree:
            if self.is_iterable(t) and len(t) > 0:
                r.extend(self.search(t, *macros))
                if t[0] in macros:
                    r.append(t)
            else:
                pass
        return(r)

    def search_env(self, tree=None, *envs):
        """Search all the ENVS environment occurence in TREE."""
        tree = tree or self.ftree.lex
        r = []
        for t in tree:
            if self.is_iterable(t) and len(t) > 0:
                r.extend(self.search_env(t, *envs))
                try:
                    if t.get('M') == 'begin':
                        if t.E.C in envs:
                            r.append(t)
                except AttributeError:
                    pass
            else:
                pass
        return(r)

    def modify_macro(self, tree,
                     args=False, macro=False):
        """Modify macro call."""
        if macro is not False:
            tree[0] = macro
        if args is not False:
            if isinstance(args, list):
                for j in args:
                    self.modify_macro(tree, args=j)
            else:
                j, rep = args
                tree[j][-1][1:-1] = rep

    def modify_env(self, tree,
                   body=False, args=False, name=False):
        """Modify environement elements.

        BODY, ARGS, NAME are removed if None,
        skipped if False, otherwise replaced.

        CAUTION: Modification of ParseResults is not fully functional.
        """

        pos_n = 1
        # pos_a = 2
        # pos_c = 3
        pos_e = -1
        if 'P' in tree:
            pos_a = 2
            pos_c = 3
        else:
            pos_a = None
            pos_c = 2

        if body is not False:
            # for j in range(4):
            #     print((j, tree[j]))
            body = body or []
            rep = pp.ParseResults(toklist=body)
            tree[pos_c:pos_e] = rep
            tree['B'] = rep
            # print(tree)
            # NOT WORKS:  tree.B = rep

        if name is not False:
            rep = pp.ParseResults(toklist=name)
            tree[pos_n][-2] = rep
            tree[pos_e][1][-2] = rep
            # print(tree.begin)
            # print(tree.end)
        else:
            # print(tree[pos_b], tree[pos_e])
            pass

        if args is not False:
            rep = pp.ParseResults(toklist=args)
            tree.args = rep
            tree[pos_a] = rep
        # tree[:] = ntree
        # print(self.unparse(ntree))
        return

    def get_parameter(self, tree, j, content=True, unparse=False):
        """Get j-th macro parameter from TREE."""
        r = None
        if j > 0:
            p = r'#%d' % j
            r = tree.P.get(p, None)
            if r:
                if content:
                    r = r.C
                else:
                    r = r.A
        if unparse and not isinstance(r, str):
            r = self.unparse(r)
        return(r)

    def parse_string(self, string, *args, **kw):
        """Run parseString() and adjust tree."""
        return(self.lex.parseString(string, *args, **kw))
        # self.orig =
        # self.post_parse()

    def parse_file(self, file, *args, **kw):
        """Run parseFile() and adjust tree."""
        if self.ftree is None:
            self.ftree = FileTree(file)
        else:
            # print('before', self.ftree.file)
            self.ftree = self.ftree.add(file)
            # print('after', self.ftree.file)

        cf = self.ftree
        results = self.lex.parseFile(file, *args, **kw)
        cf.lex = results
        # print('PARSE:', file, cf.file)
        if cf.parent:
            self.ftree = cf.parent
        if self.include < 3 or cf.parent is None:
            self.post_parse(orig=cf.lex)
        if cf.parent is None:
            self.post_parse_root(orig=cf.lex)

        return(results)

    def add_parse_action(self, m, *args):
        """Run addParseAction() on macro M or env E."""
        for pe in self.get_pe(m):
            pe.addParseAction(*args)

    def set_parse_action(self, m, *args):
        """Run setParseAction() on macro M or env E."""
        for pe in self.get_pe(m):
            pe.setParseAction(*args)

    def get_pe(self, m):
        """Search ParserElement table."""
        r = []
        if self.is_iterable(m):
            for a in m:
                r.extend(self.get_pe(a))
        elif m in self.pe_macros:
            r.append(self.pe_macros[m])
        elif m in self.pe_envs:
            r.append(self.pe_envs[m])
        else:
            sys.stderr.write('Unregistered macro %s\n' % m)
            sys.exit(1)
        return(r)

    def append_report(self, msg, s, loc, toks):
        """Append a report line."""
        lno = pp.lineno(loc, s)
        cno = pp.col(loc, s)
        line = pp.line(loc, s)
        self.report[loc] = "[%d:%d] %s: %s" % (lno, cno, msg, line)
        return

    def post_parse(self, orig=None):
        """Postproccess after parser."""

        for k in sorted(self.report.keys()):
            sys.stderr.write('%s\n' % self.report[k])

    def post_parse_root(self, orig=None):
        """Postproccess after parser (for root)."""

        pass

    def write(self, file=None, all=None, tree=None):
        """Write results to file."""
        file = file or sys.stdout
        if all:
            for f in self.ftree.root.walk():
                print(f'%%%%% {f.file}')
                tree = f.lex
                file.write(''.join(self.flatten(tree)))
        else:
            f = self.ftree.root
            tree = f.lex
            file.write(''.join(self.flatten(tree)))

    def strip(self, items, elem=None):
        """Strip all the blanks."""
        if elem is None:
            r = self.strip(items, 0)
            r = self.strip(r, -1)
            return(r)
        else:
            # print(repr(items), items)
            if isinstance(items, str):
                if elem == 0:
                    return(items.lstrip())
                elif elem == -1:
                    return(items.rstrip())
            else:
                r = items
                # print("I: ", r)
                while r:
                    b = self.strip(r[elem], elem)
                    r[elem] = b
                    if b == '':
                        r.pop(elem)
                    else:
                        break
                # print("O: ", r)
                return(r)

    def unparse(self, items, compact=False, sfx=None):
        """Unparse lex trees to string."""
        if self.is_iterable(items):
            r = ''.join(str(s) for s in self.flatten(items))
        else:
            r = items
        if compact:
            r = str(r).replace('\n', '  ')
            if isinstance(compact, int):
                if len(r) > compact:
                    r = r[:compact] + (sfx or '')
            return(r)
        else:
            return(str(r))

    def flatten(self, items):
        """Flatten input list but string."""
        for x in items:
            if hasattr(x, '__iter__') and not isinstance(x, str):
                for y in self.flatten(x):
                    yield y
            else:
                yield x

    def is_iterable(self, e):
        """Check if E is iterable not string."""
        if isinstance(e, str):
            return(False)
        return(isinstance(e, collections.abc.Iterable))

    def dump_result(self, obj):
        """Help json.dump."""
        if isinstance(obj, pp.ParseResults):
            return(obj.asList())

    def dump(self, of=None, append=None):
        """Dump results to file."""
        of = of or sys.stdout
        cache = self.cache
        if append:
            cache.update(append)
        json.dump(cache, of,
                  default=self.dump_result,
                  sort_keys=True, indent=1, ensure_ascii=False)

    def diag(self, dump=False, tree=False, *args, **kw):
        """Diagnose original structure."""
        print('%%% files')
        ppr.pprint(self.ftree.root.aslist())

        if dump:
            print('%%% dump')
            for f in self.ftree.root.walk():
                print(f'%% {f.file}')
                print(f.lex.dump())
        # print('### tree %s', self.file)
        if tree:
            print('%%% tree')
            for f in self.ftree.root:
                print(f'%% {f.file}')
                ppr.pprint(f.lex.asList(), indent=2)


class ParserStd(LexerBase):
    """Basic parser class for LaTeX document."""

    def __init__(self,
                 include=False, expand=False,
                 macros=None, envs=None, arrays=None, *args, **kw):
        """Initialize pyparsing definition."""
        envs = envs or {}
        macros = macros or {}
        arrays = arrays or {}

        # standard macros
        macros.setdefault('documentclass', [2, 1])
        macros.setdefault('usepackage', [2, 1])
        macros.setdefault('label', 1)
        macros.setdefault('nonumber', 0)
        macros.setdefault('caption', [2, 1])
        macros.setdefault('ref', 1)
        macros.setdefault('input', 1)
        macros.setdefault('cite', [2, 1])
        macros.setdefault('include', 1)
        macros.setdefault('includeonly', 1)
        macros.setdefault('newcommand', [4, 2, 3])
        macros.setdefault('newenvironment', [5, 2, 3])

        arrays.setdefault('tabular',  [2, 1])  # [ ]{2}
        arrays.setdefault('tabular*', [3, 2])  # {1}[ ]{3}

        self.figs = ['figure', 'figure*']
        for m in self.figs:
            envs.setdefault(m,   [1, 1])  # [ ]

        self.tabs = ['table', 'table*']
        for m in self.tabs:
            envs.setdefault(m,   [1, 1])  # [ ]

        self.matharrays = ['eqnarray',
                           'split', 'align', 'gather', ]
        self.eqs = ['equation'] + self.matharrays

        for m in self.matharrays:
            arrays.setdefault(m,  0)
            arrays.setdefault(m + '*',  0)
        for m in self.eqs:
            if m in self.matharrays:
                continue
            envs.setdefault(m,  0)
            envs.setdefault(m + '*',  0)

        macros.setdefault('bibliographystyle', 1)
        macros.setdefault('bibliography', 1)
        # natbib
        macros.setdefault('citet', [2, 1])
        macros.setdefault('citep', [3, 1, 2])

        # graphicx
        macros.setdefault('includegraphics', [2, 1])

        # xargs
        macros.setdefault('newcommandx', [4, 2, 3])
        macros.setdefault('newenvironmentx', [5, 2, 3])

        # section macros
        self.elevels = [True]
        self.sects = [r'chapter', r'section', r'subsection',
                      r'subsubsection', ]
        for m in self.sects:
            macros.setdefault(m, [2, 1])

        # counters
        self.ckey = {}
        for m in self.sects:
            self.ckey[m] = 'sec'
        for m in self.eqs:
            self.ckey[m] = 'eq'
        for m in self.tabs:
            self.ckey[m] = 'tab'
        for m in self.figs:
            self.ckey[m] = 'fig'

        self.counters = {'sec': 0,
                         'eq': 0,
                         'fig': 0,
                         'tab': 0, }
        self.tbl_labels = {}

        super().__init__(macros=macros, envs=envs, arrays=arrays,
                         *args, **kw)

        for m in self.sects:
            self.add_parse_action(m, self.action_section)

        self.add_parse_action('label', self.action_label)

        for m in itertools.chain(self.eqs, self.tabs, self.figs):
            self.add_parse_action(m, self.action_counter)

        # include None or 0:    skip
        #         1:            parse only
        #         2:            parse and comment out
        #         3:            parse and insert
        self.include = include or 0
        if self.include > 0:
            self.set_parse_action([r'input', r'include'],
                                  self.action_include)
        if expand:
            self.set_parse_action('newcommand', self.action_newcommand)
            self.pe_motf = []
            self.motf_defn = {}

        self.cr.addParseAction(self.action_cr)

        # self.set_parse_action('tabular', self.action_dummy)

    def action_label(self, s, loc, toks):
        r"""Control \label."""
        lab = toks.P.get('#1')
        if lab:
            lab = self.unparse(lab.get('C'))
        if lab not in self.tbl_labels:
            e = self.cenv[-1]
            k = self.ckey.get(e)
            if k:
                c = self.counters[k] + 1
            else:
                c = False
            if self.verbose > 1:
                print('label[%s]: %d' % (lab, c))
            if lab:
                self.tbl_labels[lab] = (k, c)
        # ppr.pprint(self.counters)

    def action_counter(self, s, loc, toks):
        r"""Increase counters."""
        e = toks.E.C
        if e in self.matharrays:
            pass
        else:
            k = self.ckey.get(e)
            if k:
                self.counters[k] = self.counters[k] + 1
                if self.verbose > 1:
                    print(k, self.counters[k],
                          self.unparse(toks.B, compact=30, sfx='...'))

    def action_array_row(self, s, loc, toks):
        r"""Control row in array-like environment."""
        e = self.cenv[-1]
        if e in self.matharrays:
            k = self.ckey.get(e)
            lab = self.search(r'\label')
            if lab:
                lab = toks.P.get('#1')
            if lab:
                lab = self.unparse(lab.get('C'))
            if not self.search(toks, r'\nonumber'):
                self.counters[k] = self.counters[k] + 1
                c = self.counters[k]
                if lab:
                    self.tbl_labels[lab] = (k, c)
            else:
                c = None
            if self.verbose > 1:
                print(k, c, self.unparse(toks, compact=30, sfx='...'))

    def action_cr(self, s, loc, toks):
        r"""Control \\ in some environemnts."""
        # e = self.cenv[-1]
        # if e in self.matharrays:
        #     k = self.ckey.get(e)
        #     self.counters[k] = self.counters[k] + 1

    def action_include(self, s, loc, toks):
        r"""Perform \include FILE."""
        e = ''
        if toks['M'] == r'include':
            e = '.tex'
        incf = self.unparse(toks.P['#1']['C']) + e
        if not os.path.exists(incf):
            parent = os.path.dirname(self.ftree.file)
            incf = os.path.join(parent, os.path.basename(incf))
        if self.verbose > -2:
            print(f'% Read {incf}')
        ilex = self.parse_file(incf)
        if self.include == 1:
            return(None)
        else:
            mark = '% ' + self.unparse(toks) + '\n'
            mark = self.parse_string(mark)
            if self.include == 2:
                return(mark)
            else:
                toks = pp.ParseResults(toklist=[mark, ilex])
                return(toks)

    def action_newcommand(self, s, loc, toks):
        r"""Perform newcommand on the fly."""
        # print(toks.dump())
        m = self.unparse(toks.P['#1']['C'])
        m = m[1:]
        npar = toks.P.get('#2')
        if npar:
            npar = int(self.unparse(npar['C']))
        else:
            npar = 0
        opt = toks.P.get('#3')
        if opt:
            odef = opt.get('C')
            if odef:
                odef = self.unparse(odef)
            else:
                odef = ''
        else:
            odef = None
        if opt:
            args = [npar, 1]
        else:
            args = npar
        defn = toks.P.get('#4')
        if defn:
            defn = defn.get('C')
        defn = defn or ''
        # print(m, npar, opt, odef, defn)
        lex = self.lex_macro(m, args)
        lex.setParseAction(self.action_expansion)
        self.pe_motf.append(lex)
        self.motf_defn[m] = (odef, defn)

        self.motf << pp.MatchFirst([pp.Group(e)
                                    for e in self.pe_motf])

        return(None)

    def action_expansion(self, s, loc, toks):
        r"""Perform expansion on the fly."""
        m = toks.M
        if (m or '') == '':
            m = toks.T.M
        if m:
            args = {}
            odef, defn = self.motf_defn[m]
            if toks.P:
                for k in toks.P.keys():
                    # print(toks.P[k][0].dump())
                    args[k] = toks.P[k][0].get('C', '')
                if odef is None:
                    pass
                else:
                    args['#1'] = args.get('#1') or odef
            for k in args:
                args[k] = self.unparse(args[k])
            rep = []
            for e in self.flatten(defn):
                if e in args.keys():
                    e = args[e]
                rep.append(e)
            # print(m, defn, args, rep)
            rep = self.unparse(rep)
            toks = self.parse_string(rep)
            pass
            # print(m, self.motf_defn[m])
        else:
            pass
            # print(m, toks.dump())
        return(toks)

    def action_dummy(self, s, loc, toks):
        """Perform dummy action."""
        print('DUMMY', loc)
        print(toks.dump())

    def adj_tabular(self, orig=None):
        r"""Adjust tabular environement structure.

        new CONTENTS = [[[COL] & [COL] & ... \\ ]
                        [[COL] & [COL] & ... \\ ]
                        ....]

        todo: \hline, \multicolumn, \multirow.
        """
        orig = orig or self.ftree.lex
        for env in ['tabular']:
            for tenv in self.search_env(orig, env):
                tbl = []
                row = []
                cell = []
                for tj in tenv.B:
                    if tj == r'&':
                        cell = pp.ParseResults(toklist=cell)
                        row.extend([cell, tj])
                        cell = []
                    elif tj == '\\\\':
                        if cell:
                            cell = pp.ParseResults(toklist=cell)
                            row.extend([cell, tj])
                            cell = []
                        row = pp.ParseResults(toklist=row)
                        tbl.append(row)
                        row = []
                        pass
                    else:
                        cell.append(tj)
                if cell:
                    cell = pp.ParseResults(toklist=cell)
                    row.append(cell)
                if row:
                    row = pp.ParseResults(toklist=row)
                    tbl.append(row)
                self.modify_env(tenv, body=pp.ParseResults(toklist=tbl))


class ParserAux(ParserStd):
    """Basic parser class for LaTeX .aux file."""

    def __init__(self, macros=None, envs=None, arrays=None, *args, **kw):
        """Initialize pyparsing definition."""
        envs = envs or {}
        macros = macros or {}
        arrays = arrays or {}

        macros.setdefault('newlabel', 2)

        super().__init__(macros=macros, envs=envs, arrays=arrays,
                         *args, **kw)

        self.set_parse_action('newlabel', self.action_newlabel)

        self.labels = {}

    def action_newlabel(self, s, loc, toks):
        r"""\newlabel parser."""
        lab = self.get_parameter(toks, 1, unparse=True)
        np = self.get_parameter(toks, 2)
        # print(lab)
        if np:
            nums = self.unparse(np[0].get('C', ''))
            page = self.unparse(np[1].get('C', ''))
        else:
            nums, page = None, None
        self.labels[lab] = (nums, page)

        return None

    def diag(self, *args, **kw):
        """Diagnose labels."""
        super().diag(*args, **kw)
        print("## Labels""")
        ppr.pprint(self.labels, indent=2)


def main(args, run):
    """Test lexer."""
    try:
        opts, args = getopt.getopt(args, 'vqc:ixa',
                                   ['debug',
                                    'verbose', 'quiet',
                                    'include', 'expand', 'all',
                                    'class=', ])
    except getopt.GetoptError as err:
        print(err)
        raise
    debug = False
    vlev = 0
    inc = None
    expn = False
    ctbl = {'b': (LexerBase, False),
            't': (ParserStd, False),
            's': (ParserStd, True),
            'a': (ParserAux, True), }

    ckey = True                 # auto
    out_all = False
    for o, a in opts:
        if o in ['-v', '--verbose']:
            vlev = max(0, vlev) + 1
        elif o in ['-q', '--quiet']:
            vlev = min(0, vlev) - 1
        elif o in ['--debug']:
            debug = True
        elif o in ['-i', '--include']:
            inc = (inc or 0) + 1
        elif o in ['-a', '--all']:
            out_all = True
        elif o in ['-x', '--expand']:
            expn = True
        elif o in ['-c', '--class']:
            if a not in ctbl:
                sys.stderr.write('Unknown class type [%s]\n' % a)
                sys.exit(1)
            ckey = a

    for f in args:
        k = ckey
        if k is True:
            e = os.path.splitext(f)[1]
            k = None
            if e in ['.aux']:
                k = 'a'
            elif e in ['.sty', '.cls']:
                k = 's'
            elif e in ['.tex']:
                k = 't'
        clex, atsw = ctbl[k]

        lb = clex(atletter=atsw, include=inc, expand=expn,
                  debug=debug)
        try:
            lb.parse_file(f, parseAll=True)
        except Exception as e:
            sys.stderr.write('Panic in %s [%s]\n' % (f, e.args))
            raise

        if vlev > 1:
            lb.diag()
        lb.write(all=out_all)
    pass


if __name__ == '__main__':
    main(sys.argv[1:], run=sys.argv[0])
    pass
