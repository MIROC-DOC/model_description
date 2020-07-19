#!/usr/bin/env python3
# Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>
# 'Time-stamp: <2020/07/14 09:41:01 fuyuki lexer.py>'

import sys
import pprint as ppr
import collections.abc
import json
import string
import getopt

import pyparsing as pp
# pp.ParserElement.enablePackrat()   # does not help, even worse


class LexerBase:
    """Core lexer class for LaTeX document."""

    def __init__(self,
                 macros=None, envs=None,
                 atletter=False,
                 debug=False, **kw):
        """Initialize pyparsing definition."""
        default_whites = pp.ParserElement.DEFAULT_WHITE_CHARS
        pp.ParserElement.setDefaultWhitespaceChars('')

        macros = macros or {}
        envs = envs or {}
        self.debug = debug
        self.report = {}

        self.cache = {}

        uc_whites = [chr(12288)]
        # 12288: 2 byte white space [　]
        uc_puncts = []

        ctl = '\\'              # catcode 0
        lbr = r'{'              # catcode 1
        rbr = r'}'              # catcode 2
        com = r'%'              # catcode 14
        mxp = r'$'              # catcode 3

        amp = r'&'              # catcode 4
        lbs = r'['
        rbs = r']'
        par = r'#'              # catcode 6

        excl = [com, ctl, lbr, rbr, mxp, amp, lbs, rbs, par]

        # (a part of) TeX special charcters % \ { } $ #&~_^

        self.com = pp.Literal(com)
        self.ctl = pp.Literal(ctl)
        self.lbr = pp.Literal(lbr)
        self.rbr = pp.Literal(rbr)
        self.mxp = pp.Literal(mxp)

        # symbols
        self.amp = pp.Literal(amp)
        self.lbs = pp.Literal(lbs)
        self.rbs = pp.Literal(rbs)
        self.par = pp.Literal(par)
        # single-char symbols
        self.ssym = pp.MatchFirst([self.amp, self.lbs, self.rbs])

        # nl
        self.nl = pp.LineEnd()
        # ws
        self.ws = pp.White()
        # comment line
        self.cline = pp.Combine(self.com + pp.restOfLine() + self.nl)

        # letters
        self.letters = pp.Forward()
        # cseq
        self.cseq = pp.Combine(self.ctl + self.letters)

        self.atletter = pp.Group(pp.Combine(self.ctl
                                            + pp.Literal('makeatletter')))
        self.atother = pp.Group(pp.Combine(self.ctl
                                           + pp.Literal('makeatother')))

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
        # string.punctuation
        self.esym = pp.MatchFirst([pp.Combine(pp.Literal(ctl + ch))
                                   for ch in string.punctuation + ' '
                                   if ch not in [lbs, rbs]])

        self.usym = pp.MatchFirst([pp.Combine(pp.Literal(ctl + ch))
                                   for ch in uc_puncts])

        # special whitespace
        self.uws = pp.oneOf(uc_whites)

        # normal
        self.atext = pp.Combine(pp.Word(pp.printables + ' ',
                                        excludeChars=''.join(excl))
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

        # \begin \end
        self.benv = pp.Group(self.lex_begin() + pp.Group(pp.Empty()))
        self.eenv = pp.Group(self.lex_end())

        self.benv.setParseAction(self.action_unmatched)
        self.eenv.setParseAction(self.action_unmatched)

        # \verb
        verb_head = (pp.Combine(self.ctl + pp.Literal(r'verb'))
                     + (pp.Char(string.punctuation)
                        | pp.Literal(' ') | pp.Literal('\n')))
        verb_foot = pp.Forward()

        def action_endverb(toks):
            r"""Emulate \verb."""
            right = pp.Literal(toks[-1])
            term = right.copy()
            term.setParseAction(action_term)
            e = (right | pp.StringEnd())
            ee = (term | pp.StringEnd())
            verb_foot << pp.Combine(pp.Optional(self.ws) + pp.SkipTo(e) + ee)

        verb_head.setParseAction(action_endverb)
        vlex = verb_head + verb_foot

        def adj_verb(s, loc, toks):
            r"""Adjust verbatim string."""
            if 'closed' in toks:
                e = toks[-1][-1]
                toks[-1] = toks[-1][:-1]
                toks.append(e)
            else:
                ln = pp.lineno(loc, s)
                cn = pp.col(loc, s)
                line = pp.line(loc, s)
                self.report[loc] = ('Unclosed %s at %d:%d %s'
                                    % (toks[0], ln, cn, line))
            return(toks)

        vlex.setParseAction(adj_verb)

        # todo  <\verb  >  cannot be handled  (i.e., \verb SPACE null SPACE)
        vsp2 = pp.Literal(r'\verb  ') | pp.Literal(r'\verb\n\n')
        vnl2 = pp.Combine(pp.Literal(r'\verb') + pp.LineEnd() + pp.LineEnd())

        self.verb = pp.Group(vsp2 | vnl2 | vlex)

        # def
        self.def_def = self.lex_def(r'def')

        # macros
        self.macros = [self.atletter, self.atother, self.def_def]
        for m, a in macros.items():
            self.macros.append(self.lex_macro(m, a))

        self.mlex = pp.MatchFirst(self.macros)

        # environments
        envs.setdefault('tabular',  [2, 1])  # [ ]{2}
        envs.setdefault('tabular*', [3, 2])  # {1}[ ]{3}

        # self.envs = {ENV: (LEXER, PROP)}
        eall = []
        self.envs = {}
        for e, a in envs.items():
            lp = self.lex_env_group(e, a)
            self.envs[e] = (lp, a)
            eall.append(lp)
            if debug:
                lp.setDebug()
        # default environment
        lp = self.lex_env_group(None)
        if self.debug:
            lp.setDebug()
        self.envs[None] = (lp, None)
        eall.append(lp)

        self.elex = pp.MatchFirst(eall)

        # fallback
        self.fallback = pp.Combine(self.ctl + pp.Regex('.')) | pp.Regex('.')
        self.fallback.setParseAction(self.action_fallback)

        # expr
        self.expr = (self.normal
                     | self.mlex
                     | self.verb
                     | self.elex
                     | self.benv | self.eenv
                     | self.cseq | self.esym | self.ssym
                     | self.imath | self.dmath | self.xmath
                     | self.group
                     | self.nl | self.ws
                     | self.cline
                     | self.posp
                     | self.uws | self.usym
                     | self.fallback)

        def action_term(toks):
            """Mark correct closing."""
            toks['closed'] = ''
            return(toks)

        def gen_group(left, right=None):
            """Generate grouped token wtih LEFT RIGHT delimiters."""
            right = (right or left).copy()
            term = right.copy()
            term.setParseAction(action_term)
            g = (left
                 + pp.ZeroOrMore(~right + self.expr)
                 + (term | pp.StringEnd()))
            g.setParseAction(self.action_group)
            return(pp.Group(g))

        # group { }
        self.group << gen_group(self.lbr, self.rbr)
        # opt [ ]
        self.opt << gen_group(self.lbs, self.rbs)
        # inline math $ $
        self.imath << gen_group(self.mxp)
        # display math $$ $$
        self.dmx = pp.Literal(mxp + mxp)
        self.xmath << gen_group(self.dmx)
        # display math \[ \]
        self.ldm = pp.Literal(ctl + lbs)
        self.rdm = pp.Literal(ctl + rbs)

        self.dmath << gen_group(self.ldm, self.rdm)

        # Important: self.letters must be defined after def_def.
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
                if debug:
                    lp.setDebug()
        #
        pp.ParserElement.setDefaultWhitespaceChars(default_whites)
        return

    def action_fallback(self, s, loc, toks):
        """Remember fallback token."""
        ln = pp.lineno(loc, s)
        cn = pp.col(loc, s)
        line = pp.line(loc, s)
        self.report[loc] = ('Fallback [%s] at %d:%d %s'
                            % (toks[0], ln, cn, line))
        return

    def action_group(self, s, loc, toks):
        """Check if closed."""
        if 'closed' in toks:
            pass
        else:
            ln = pp.lineno(loc, s)
            cn = pp.col(loc, s)
            line = pp.line(loc, s)
            self.report[loc] = ('Unclosed %s at %d:%d %s'
                                % (toks[0], ln, cn, line))
        return

    def action_unmatched(self, s, loc, toks):
        """Remember unmatched token."""
        ln = pp.lineno(loc, s)
        cn = pp.col(loc, s)
        self.report[loc] = ('Unmatched %s{%s} at %d:%d'
                            % (toks[0][0], toks[0].env.name, ln, cn))
        return

    def lex_def(self, name, macro=None, args=None):
        r"""Define lexer for \def\macro...{content}."""
        macro = macro or r'def'
        args = args or 1

        cs = pp.Combine(self.ctl + pp.Literal(macro))
        name = pp.Combine(self.ctl + self.letters)
        pl = [pp.Combine(self.par + pp.Literal('%d' % j))
              for j in range(1, 10)]
        sep = pp.SkipTo((self.lbr | self.par))
        par = pp.Optional(pl[-1] + sep)
        for j in reversed(pl[:-1]):
            par = pp.Optional(j + sep + par)
        ptm = pp.Combine(self.par + pp.FollowedBy(self.lbr))
        alex = self.gen_aset(args)
        lex = pp.Group(cs + name
                       + pp.Group(sep + pp.Optional(par) + pp.Optional(ptm))
                       + alex)
        return(lex)

    def lex_begin(self, name=None):
        r"""Define lexer for \begin{NAME} starter."""
        begin = pp.Combine(self.ctl + pp.Literal(r'begin'))
        if isinstance(name, str):
            name = pp.Literal(name)
        elif name is None:
            name = pp.Word(pp.alphas + '*')
        earg = (self.blanks
                + self.lbr + name.setResultsName('name') + self.rbr)

        lex = begin + pp.Group(earg).setResultsName('env')
        return(lex.setResultsName('begin'))

    def lex_end(self, name=None):
        r"""Define lexer for \end{NAME}."""
        end = pp.Combine(self.ctl + pp.Literal(r'end'))
        if isinstance(name, str):
            name = pp.Literal(name)
        elif name is None:
            name = pp.Word(pp.alphas + '*')
        earg = (self.blanks
                + self.lbr + name.setResultsName('name') + self.rbr)
        lex = end + pp.Group(earg).setResultsName('env')
        return(lex.setResultsName('end'))

    def lex_env_group(self, name, args=None):
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

        if name is None:
            envgroup.setName('ENV')
        else:
            envgroup.setName('ENV/%s' % name)

        open_env = self.lex_begin(name)
        close_env = pp.Forward()

        def gen_close(toks):
            """Close environemnt."""
            e = toks.env.name
            c = pp.Group(self.lex_end(e))
            contents = pp.ZeroOrMore(~c + self.expr).setResultsName('contents')
            close_env << (contents + c.setResultsName('end'))

        open_env.setParseAction(gen_close)

        alex = self.gen_aset(args)

        # [r'\begin', [ENV], [ARG], CONTENT..., [r'\end', [ENV]]]
        envgroup << pp.Group(open_env.setResultsName('begin')
                             + pp.Group(alex).setResultsName('args')
                             + close_env)
        return(envgroup)

    def lex_macro(self, macro, args=None):
        r"""Define lexer for tex typical macro with arguments.

        Todo: * is not treated.
              ungrouped arguments are not treated.

        """
        cs = pp.Combine(self.ctl + pp.Literal(macro) + ~self.letters)

        alex = self.gen_aset(args)

        lex = pp.Group(cs + pp.Group(alex))
        lex.setName('MACRO/%s' % macro)
        # ['MACRO', [[ARG], [ARG], ...]]
        return(lex)

    def gen_aset(self, args=None):
        """Generate option/parameter list."""
        # Todo: optional arguments if not separated by blank
        # Todo: xparse type arguments list
        # (e.g., frame in beamer class)
        # True: {mandatory}   False: [optional]
        if args is None:
            args = [0]
        elif isinstance(args, int):
            args = [args]
        # None is sentry (start=1)
        aset = [None] + [True] * args[0]
        for a in args[1:]:
            aset[a] = False

        alex = []
        for a in aset[1:]:
            if a:
                alex.append(pp.Group(self.blanks + self.group))
            else:
                alex.append(pp.Group(pp.Optional(self.blanks + self.opt)))
        if alex:
            alex = pp.And(alex)
        else:
            alex = pp.Empty()

        return(alex)

    def search(self, tree=None, *macros):
        """Search all the MACROS occurence in TREE.

        Macro in MACROS must be defined in LexerBase if with arguments.
        Only registered macros can be searched.
        """
        tree = tree or self.orig
        r = []
        for t in tree:
            if self.is_iterable(t) and len(t) > 0:
                # ppr.pprint(t, compact=True, indent=2)
                if t[0] in macros:
                    r.append(t)
                r[-1:-1] = self.search(t, *macros)
                # r.extend(self.search_env(t, *envs))
            else:
                # if t in macros:
                #     r.append(t)
                pass
        return(r)

    def search_env(self, tree=None, *envs):
        """Search all the ENVS environment occurence in TREE."""
        tree = tree or self.orig
        r = []
        # [\begin [WS { ENV }] ... ]
        for t in tree:
            if self.is_iterable(t) and len(t) > 0:
                # ppr.pprint(t, compact=True, indent=2)
                if 'begin' in t:
                    if t.env.name in envs:
                        r.append(t)
                # r[-1:-1] = self.search_env(t, *envs)
                r.extend(self.search_env(t, *envs))
            else:
                pass
        return(r)

    def modify_env(self, tree,
                   contents=False, args=False, name=False):
        """Modify environement elements.

        CONTENTS, ARGS, NAME are removed if None,
        skipped if False, otherwise replaced.
        """
        pos_b = 0
        pos_n = 1
        pos_a = 2
        pos_c = 3
        pos_e = -1

        if contents is False:
            pass
        else:
            contents = contents or []
            rep = pp.ParseResults(toklist=contents)
            tree[pos_c:pos_e] = rep
            tree.contents = rep

        if name is False:
            pass
        elif name:
            rep = pp.ParseResults(toklist=name)
            tree[pos_n][-2] = rep
            tree[pos_e][1][-2] = rep
            # print(tree.begin)
            # print(tree.end)
        else:
            print(tree[pos_b], tree[pos_e])
            pass

        if args is False:
            pass
        else:
            rep = pp.ParseResults(toklist=args)
            tree.args = rep
            tree[pos_a] = rep

        return

    def parse_string(self, string, *args, **kw):
        """Run parseString() and adjust tree."""
        self.orig = self.lex.parseString(string, *args, **kw)
        self.post_parse()

    def parse_file(self, file, *args, **kw):
        """Run parseFile() and adjust tree."""
        self.orig = self.lex.parseFile(file, *args, **kw)
        self.post_parse()

    def post_parse(self, orig=None):
        """Postproccess after parser."""
        orig = orig or self.orig
        self.cache['tree'] = orig.asList()

        for k in sorted(self.report.keys()):
            sys.stderr.write('%s\n' % self.report[k])

    def write(self, file=None, tree=None):
        """Write results to file."""
        file = file or sys.stdout
        tree = tree or self.orig

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

    def unparse(self, items):
        """Unparse lex trees to string."""
        if self.is_iterable(items):
            return(''.join([str(s) for s in self.flatten(items)]))
        else:
            return(str(items))

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

    def diag(self, tree=None, aslist=True, *args, **kw):
        """Diagnose original structure."""
        tree = tree or self.orig
        if aslist:
            t = tree.asList()
        else:
            t = tree
        ppr.pprint(t, indent=2)


class LexerStd(LexerBase):
    """Basic lexer class for LaTeX document."""

    def __init__(self,
                 macros=None, envs=None, **kw):
        """Initialize pyparsing definition."""
        envs = envs or {}
        macros = macros or {}

        # standard macros
        macros.setdefault('documentclass', [2, 1])
        macros.setdefault('usepackage', [2, 1])
        macros.setdefault('label', 1)
        macros.setdefault('ref', 1)
        macros.setdefault('newcommand', [4, 2, 3])
        macros.setdefault('newenvironment', [5, 2, 3])
        envs.setdefault('tabular',  [2, 1])  # [ ]{2}
        envs.setdefault('tabular*', [3, 2])  # {1}[ ]{3}

        # natbib
        macros.setdefault('citet', [2, 1])
        macros.setdefault('citep', [3, 1, 2])

        # graphicx
        macros.setdefault('includegraphics', [2, 1])

        # xargs
        macros.setdefault('newcommandx', [4, 2, 3])
        macros.setdefault('newenvironmentx', [5, 2, 3])

        super().__init__(macros=macros, envs=envs, **kw)

    def post_parse(self, orig=None):
        """Postproccess after parser."""
        orig = orig or self.orig
        super().post_parse(orig=orig)
        self.adj_tabular()

    def adj_tabular(self, orig=None):
        r"""Adjust tabular environement structure.

        new CONTENTS = [[[COL] & [COL] & ... \\ ]
                        [[COL] & [COL] & ... \\ ]
                        ....]

        todo: \hline, \multicolumn, \multirow.
        """
        orig = orig or self.orig
        for env in ['tabular']:
            for tenv in self.search_env(orig, env):
                # ppr.pprint(list(tenv.items()))
                # ppr.pprint(tenv.asList())
                tbl = []
                row = []
                cell = []
                for tj in tenv.contents:
                    if tj == r'&':
                        row.extend([cell, tj])
                        cell = []
                    elif tj == '\\\\':
                        if cell:
                            row.extend([cell, tj])
                            cell = []
                        tbl.append(row)
                        row = []
                        pass
                    else:
                        # print(type(tj), tj)
                        cell.append(tj)
                if cell:
                    row.append(cell)
                if row:
                    tbl.append(row)
                self.modify_env(tenv, contents=tbl)


def main(args, run):
    """Test lexer."""
    try:
        opts, args = getopt.getopt(args, 'vq',
                                   ['verbose', 'quiet', 'debug'])
    except getopt.GetoptError as err:
        print(err)
        raise
    debug = False
    vlev = 0
    for o, a in opts:
        if o in ['-v', '--verbose']:
            vlev = max(0, vlev) + 1
        elif o in ['-q', '--quiet']:
            vlev = min(0, vlev) - 1
        elif o in ['--debug']:
            debug = True

    for f in args:
        print("# %s" % (f))
        lb = LexerStd(debug=debug,
                      macros={'label': 1, })
        try:
            lb.parse_file(f, parseAll=True)
        except Exception as e:
            sys.stderr.write('Panic in %s [%s]\n' % (f, e.args))
            raise

        if vlev > 0:
            lb.diag()
        lb.write()
        # lb.diag(aslist=False)
    pass


if __name__ == '__main__':
    main(sys.argv[1:], run=sys.argv[0])
    pass
