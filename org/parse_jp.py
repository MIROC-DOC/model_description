#!/usr/bin/env python3
# Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>
# 'Time-stamp: <2020/08/02 17:42:34 fuyuki evacuate.py>'

# import psitex as psi
import psitex
import sys
import getopt
import os.path
import string
import re
import pprint as ppr
import pyparsing as pp


class ParserMirocDoc(psitex.ParserStd):
    """Simple class for MIROC document replacement."""

    def __init__(self, macros=None,
                 eenv=None, etab=None,
                 math=False, label=False, ref=False, dennou=False, **kw):
        """Initialize MIROC-Doc replacement."""
        macros = macros or {}
        macros['Module'] = 1
        macros['Dvect'] = 1
        macros['DP'] = (4, 1, 2)
        macros['DD'] = (3, 1)
        macros['Dinclude'] = 1
        macros['EQN'] = 1

        super().__init__(macros=macros, **kw)

        self.dennou = dennou
        self.label = label
        self.ref = ref
        self.math = math
        self.tbl_ref = {}
        self.tbl_imath = {}
        self.tbl_emath = {}
        self.tabular = {}
        self.fmt_imath = 'TERM%05d'
        self.fmt_emath = 'EQ=%05d.'
        self.fmt_tabular = 'TAB%05d:'
        self.fmt_label = 'L%05d'
        self.fmt_ref = 'R%05d'

        self.cache.update(imath=self.tbl_imath,
                          emath=self.tbl_emath,
                          label=self.tbl_labels,
                          ref=self.tbl_ref)
        if eenv == 'q':
            eenv = 'quote'
        elif eenv in ['qn', 'qq']:
            eenv = 'quotation'
        elif eenv in ['v']:
            eenv = 'verbatim'
        if eenv not in [None, 'quote', 'quotation', 'verbatim']:
            sys.stderr.write('Invalid parameter %s\n' % eenv)
            sys.exit(1)
        self.eenv = eenv

        if etab == 'd':
            etab = 'description'
        if etab not in [None, 'description']:
            sys.stderr.write('Invalid parameter %s\n' % etab)
            sys.exit(1)
        self.etab = etab

        if self.dennou:
            self.set_parse_action(r'DP', self.action_DP)
            self.set_parse_action(r'DD', self.action_DD)
            self.set_parse_action(r'Dvect', self.action_Dvect)
            self.set_parse_action(r'Dinclude', self.action_Dinclude)

        self.set_parse_action(r'Module', self.action_module)
        # if self.label:
        #     self.add_parse_action(r'label', self.action_label)
        #     self.add_parse_action(r'ref', self.action_ref)

        pass

    def action_counter(self, s, loc, toks):
        r"""Increase counters."""
        super().action_counter(s, loc, toks)
        if self.ref or self.label:
            e = toks.E.C
            if e in self.matharrays:
                pass
            else:
                k = self.ckey.get(e)
                if k in ['eq']:
                    rep = (self.unparse(toks.B)
                           + (r' \EQN{%d}' % self.counters[k]))
                    rep = self.parse_string(rep)
                    if self.label:
                        self.modify_env(toks, body=rep)
            return(toks)

    def action_array_row(self, s, loc, toks):
        super().action_array_row(s, loc, toks)
        if self.ref or self.label:
            e = self.cenv[-1]
            if e in self.matharrays:
                k = self.ckey.get(e)
                if not self.search(toks, r'\nonumber'):
                    c = self.counters[k]
                    rep = self.unparse(toks)
                    eqn = r' \EQN{%d}' % c
                    if self.label:
                        if rep.endswith('\\\\'):
                            rep = rep[:-2] + eqn + rep[-2:]
                        else:
                            rep = rep + eqn
                    toks = self.parse_string(rep)
        return(toks)

    def action_Dinclude(self, s, loc, toks):
        r"""Replace \Dinclude expansion."""
        f = self.get_parameter(toks, 1, unparse=True) + r'.tex'
        rep = r'\include{%s}' % f
        return(self.parse_string(rep))

    def action_DP(self, s, loc, toks):
        r"""Replace \DP expansion on-the-fly."""
        a = [''] * 5
        for n in range(1, 5):
            c = toks.P.get(f'#{n}')
            if c:
                a[n] = self.unparse(c.A)

        if a[2]:
            tmpl = (r'\left(\frac{{\partial^{1}{3}}}'
                    + r'{{\partial {4}{{}}^{1}}}\right)_{2}').format(*a)
        elif a[1]:
            tmpl = (r'\frac{{\partial^{1}{3}}}'
                    + r'{{\partial {4}{{}}^{1}}}').format(*a)
        else:
            tmpl = r'\frac{{\partial{3}}}{{\partial {4}}}'.format(*a)
        tmpl = pp.ParseResults(tmpl)
        toks.T = tmpl
        toks[:] = tmpl
        return(toks)

    def action_DD(self, s, loc, toks):
        r"""Replace \DD expansion on-the-fly."""
        a = [''] * 4
        for n in range(1, 4):
            c = toks.P.get(f'#{n}')
            if c:
                a[n] = self.unparse(c.A)

        if a[1]:
            tmpl = r'\frac{{d^{1}{2}}}{{d {3}{{}}^{1}}}'.format(*a)
        else:
            tmpl = r'\frac{{d {2}}}{{d {3}}}'.format(*a)
        tmpl = pp.ParseResults(tmpl)
        toks.T = tmpl
        toks[:] = tmpl
        return(toks)

    def action_Dvect(self, s, loc, toks):
        r"""Replace \Dvect expansion on-the-fly."""
        # \def\Dvect#1{\mbox{\boldmath $#1$}}
        a = toks.P.get('#1')
        a = self.unparse(a)
        # tmpl = r'\mbox{{\boldmath ${}$}}'.format(a)
        tmpl = r'\mbox{$\mathbf%s$}' % a
        toks = self.parse_string(tmpl)
        return(toks)

    def action_module(self, s, loc, toks):
        r"""Replace \Module macros."""
        a = toks.P['#1']['C']
        arep = [r'MODULE:[', *a, ']']
        self.modify_macro(toks, macro=r'\texttt', args=[(1, arep)])
        return(toks)

    def post_parse(self, orig=None, *args, **kw):
        """Batch replacement of special macros."""
        super().post_parse(orig=orig, *args, **kw)
        if self.math:
            self.rep_imath(tree=orig)
            self.rep_enveq(tree=orig)
            self.rep_envar(tree=orig)
            self.rep_dispm(tree=orig)
        self.rep_tabular(tree=orig)

    def post_parse_root(self, *args, **kw):
        """Batch replacement of special macros (for root source)."""
        if self.ref:
            if self.include > 2:
                self.rep_ref(tree=self.ftree.root.lex)
            else:
                for f in self.ftree.root.walk():
                    self.rep_ref(tree=f.lex)

    def rep_imath(self, tree=None, fmt=None, lev=0):
        """Replace inline maths."""
        strsep = string.punctuation + string.whitespace

        tree = tree or self.ftree.lex
        fmt = fmt or self.fmt_imath
        math = False
        rsfx = re.compile('[a-zA-Z]+$')
        rpfx = re.compile(r'^[a-zA-Z]+')

        # ppr.pprint(tree.asList())
        for j, a in enumerate(tree):
            if math:
                p, m = tree[j-2:j]
                # print(p, m, a, len(self.tbl_imath))
                src = m.copy()
                txt = fmt % len(self.tbl_imath)
                rep = [txt]
                for jj in src:
                    if isinstance(jj, str) and ',' in jj:
                        rep.extend([',', txt])
                        break

                head = (isinstance(p, str)
                        and len(p) > 0 and p[-1] not in strsep)
                foot = (isinstance(a, str)
                        and len(a) > 0 and a[0] not in strsep)
                # print(lev, j, head, foot, (p, src, a))
                if head or foot:   # either concatenated
                    if head:
                        pfx = rsfx.search(p)
                    else:
                        pfx = None
                    if foot:
                        sfx = rpfx.match(a)
                    else:
                        sfx = None
                    xm = self.unparse(m[1:-1])
                    if xm.lstrip()[0] in '^_' and pfx:
                        tree[j-2] = p[:pfx.start()]
                        src.insert(0, pfx.group())
                        p = tree[j-2]
                        head = len(p) > 0 and p[-1] not in strsep
                        if sfx:
                            tree[j] = a[sfx.start()+1:]
                            src.append(sfx.group())
                            a = tree[j]
                            foot = len(a) > 0 and a[0] not in strsep
                        if pfx:
                            pfx = pfx.group()
                        if sfx:
                            sfx = sfx.group()
                        if self.verbose > -1:
                            sys.stdout.write('unit/chem token (%s:%s:%s)\n'
                                             % (pfx, xm, sfx))
                        pass
                    if head:
                        rep.insert(0, ' ')
                    if foot:
                        rep.append(' ')
                    pass
                m[:] = rep
                self.tbl_imath[txt] = (src, head, foot)
                math = False
            if self.is_iterable(a) and len(a) > 0:
                if a[0] == r'$':
                    math = True
                else:
                    self.rep_imath(a, fmt, lev + 1)
            pass
        # last block
        if math:
            sys.stderr.write('Not implemented.\n')
            pass

    def rep_enveq(self, tree=None, fmt=None):
        """Replace equation environement."""
        fmt = fmt or self.fmt_emath
        tree = tree or self.ftree.lex
        for m in self.search_env(tree, r'equation', r'equation*',
                                 r'displaymath', ):
            # lbl = self.search(m, r'\label')
            eqn = self.get_eqn(m)
            # print(eqn)
            txt = fmt % len(self.tbl_emath)
            src = m.B.copy()
            self.tbl_emath[txt] = src
            rep = ['\n', txt, eqn, '\n']
            # if len(lbl) == 1:
            #     rep.extend([lbl, '\n'])
            # elif len(lbl) > 1:
            #     ll = [''.join(self.flatten(li)) for li in lbl]
            #     sys.stderr.write('Multiple labels {%s}\n' % ' '.join(ll))
            self.modify_env(m, body=rep)
            if self.eenv:
                self.modify_env(m, name=self.eenv)

    def rep_envar(self, tree=None, fmt=None):
        """Replace eqnarray environement."""
        fmt = fmt or self.fmt_emath
        tree = tree or self.ftree.lex
        for m in self.search_env(tree, r'eqnarray', r'eqnarray*'):
            txt = fmt % len(self.tbl_emath)
            src = m.B.copy()
            self.tbl_emath[txt] = src
            rep = ['\n']
            for a in m.B:
                eqn = self.get_eqn(a)
                rep.extend([txt, eqn, '\n'])
            self.modify_env(m, body=rep)
            if self.eenv:
                self.modify_env(m, name=self.eenv)

    def get_eqn(self, tree):
        r"""Search \EQN and return its replacement."""
        eqn = self.search(tree, r'\EQN')
        if self.label:
            if eqn:
                eqn = self.get_parameter(eqn[0], 1, unparse=True)
            if eqn:
                eqn = f'    --- ({eqn})'
        else:
            eqn = None
        return(eqn or '')

    def rep_dispm(self, tree=None, fmt=None):
        r"""Replace displaymath (\[\])."""
        fmt = fmt or self.fmt_emath
        tree = tree or self.ftree.lex

        def is_ascii(s):
            return all(ord(c) < 128 for c in s)

        for m in self.search(tree, r'\['):
            # non-smart solution, to check only ascii
            con = slice(1, -1)
            src = m[con].copy()
            chk = ''.join(self.flatten(src))
            # python3.7
            # if chk.isascii():
            if is_ascii(chk):
                txt = fmt % len(self.tbl_emath)
                m[con] = ['\n', txt, '\n']
                self.tbl_emath[txt] = src
            else:
                if self.verbose > -1:
                    sys.stdout.write('Ignore displaymath %s\n' % chk)

    def rep_tabular(self, tree=None, fmt=None):
        """Replace tabular environement."""
        if self.etab is None:
            return
        if self.etab != 'description':
            return

        fmt = fmt or self.fmt_tabular
        self.cache['tabular'] = self.tabular

        tree = tree or self.ftree.lex
        for m in self.search_env(tree, 'tabular'):
            txt = fmt % len(self.tabular)
            src = m.B.copy()
            self.tabular[txt] = src

            tab = [[]]
            for line in m.B.asList():
                for e in line:
                    if e == '\\\\':
                        tab.append([])
                        pass
                    else:
                        if e[-1] == r'&':
                            e.pop(-1)
                        e = self.strip(e)
                        tab[-1].append(e)
            row, col = 0, 0
            rep = ['\n']
            # ppr.pprint(tab)
            for row, line in enumerate(tab):
                if any(line):
                    for col, e in enumerate(line):
                        label = txt + ('%d.%d' % (row, col))
                        if isinstance(e, str):
                            e = [e]
                        rep.append([r'\item',
                                    ['[', label, ']'], ' '] + e + ['\n'])
            self.modify_env(m, body=rep, name=self.etab, args=None)
            # m[2] = []

    def rep_ref(self, tree=None):
        """Replace equation environement."""
        tree = tree or self.ftree.lex
        for m in self.search(tree, r'\ref'):
            tag = self.get_parameter(m, 1, unparse=True)
            k, n = self.tbl_labels.get(tag, (None, None))
            if k in ['eq']:
                m[:] = [str(n)]
                if self.verbose > 2:
                    print(f'% Reference embedded {tag}[{k}]=={n})')
            elif self.verbose > 0:
                print(f'% skipped {tag}[{k}]=={n})')

        pass

    def write(self, outdir, outf, over=False, *args, **kw):
        """Write all the results."""
        # super().write(*args, **kw)
        if self.include > 2:
            files = [self.ftree.root]  # root only
        else:
            files = self.ftree.root.walk()    # iterate through trees

        for f in files:
            src = f.file
            tree = f.lex
            of = sys.stdout
            if outdir is False:
                of = sys.stdout
                dest = 'stdout'
            else:
                if not outf:
                    outf = os.path.basename(src)
                dest = os.path.join(outdir, outf)
                if os.path.exists(dest):
                    if os.path.samefile(src, dest):
                        sys.stderr.write('Output file is identical %s.\n'
                                         % dest)
                        sys.exit(1)
                    if not over:
                        sys.stderr.write('Exists output file %s.\n' % dest)
                        sys.exit(1)
                of = open(dest, 'w')
            if self.verbose > -2:
                print(f'% Convert {f.file} > {dest}')
            of.write(''.join(self.flatten(tree)))
            if outdir:
                of.close()
            outf = None         # clear for included files

    def diag(self, tables=False, *args, **kw):
        """Diagnostic."""
        super().diag(*args, **kw)
        if tables:
            self.diag_imath()
            self.diag_emath()
            self.diag_tabular()

    def diag_imath(self):
        """Diagnose inline maths."""
        for term in sorted(self.tbl_imath.keys()):
            if self.tbl_imath[term]:
                src, head, foot = self.tbl_imath[term]
                src = self.unparse(src).replace('\n', ' ')
                print('%s: %s  %s %s' % (term, src, head, foot))
            else:
                print('%s: (null)')

    def diag_emath(self):
        """Diagnose equations."""
        for term, src in sorted(self.tbl_emath.items()):
            if src:
                src = self.unparse(src).replace('\n', ' ')
                print('%s: %s' % (term, src))
            else:
                print('%s: (null)')

    def diag_tabular(self):
        """Diagnose equations."""
        for term, src in sorted(self.tabular.items()):
            if src:
                src = self.unparse(src).replace('\n', ' ')
                print('%s: %s' % (term, src))
            else:
                print('%s: (null)')


def show_usage(run=None, short=False, out=None):
    """Show usage."""
    out = out or sys.stdout
    run = run or ''
    out.write(f"Usage: {run} [OPTIONS]... [FILES]....\n")
    out.write("""MIROC document parser for the pushmi-pullyu project.\n""")

    if short:
        out.write(f"""run {run} -h to print the usage.\n""")
    else:
        out.write("""Input files are parsed and output to same basenames under output
directory (default `.').  If subfile-mode is enabled (-S) all
the included files are also parsed and output to their same
basenames under same output directory.
Replacement properties are output to rootname.json.

Parameters
    FILE                 source file

General options
    -h, --help           show this usage
    -v, --verbose        be more verbose
    -q, --quiet          be more silent
        --debug          enable to print debug information
    -f, --force          force overwrite if exists
    -o, --output=FILE    set output filename as FILE (single-file case)
    -d, --outdir=PATH    set PATH as output directory (must exist)
Replacement controls
    -M, --math           replace inline maths and math environements
    -D, --dennou         replace dennou macros
    -L, --label          embed labels for equations
    -R, --ref            embed references to equation labels
    -S, --subfiles       also parse included files
    -1, --onefile        expand included files to the root (imply -S)
    -E, --equation=SW    replace equation-like environments as SW
                         SW: q=quote, qq=quotation, v=verbatim
    -T, --tabular=SW     replace tabular-like environments as SW
                         SW: d=description

Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>.
This system is part of MIROC-DOC project and psiTeX project.\n""")
        pass


def main(args, run):
    """Main."""
    try:
        opts, args = getopt.getopt(args, 'hvqfo:d:MDLRS1E:T:',
                                   ['debug',
                                    'help', 'verbose', 'quiet', 'force',
                                    'output=', 'outdir=',
                                    'math', 'dennou', 'label', 'ref',
                                    'subfiles', 'onefile',
                                    'equation=', 'tabular=', ])
    except getopt.GetoptError as err:
        sys.stderr.write(str(err) + '\n')
        show_usage(run=run, short=True, out=sys.stderr)
        sys.exit(1)
    debug = False
    outdir = None
    outf = None
    overw = False
    vlev = 0
    eenv = None
    etab = None
    dennou = None
    label = None
    ref = None
    math = None
    inc = 0
    for o, a in opts:
        if o in ['-h', '--help']:
            show_usage(run)
            sys.exit(0)
        elif o in ['-d', '--outdir']:
            outdir = a
        elif o in ['-o', '--output']:
            outf = a
        elif o in ['-f', '--force']:
            overw = True
        elif o in ['-v', '--verbose']:
            vlev = max(0, vlev) + 1
        elif o in ['-q', '--quiet']:
            vlev = min(0, vlev) - 1
        elif o in ['-E', '--equation']:
            eenv = a
        elif o in ['-T', '--tabular']:
            etab = a
        elif o in ['-D', '--dennou']:
            dennou = True
        elif o in ['-S', '--subfiles']:
            inc = max(inc, 1)
        elif o in ['-1', '--onefile']:
            inc = max(inc, 3)
        elif o in ['-L', '--label']:
            label = True
        elif o in ['-R', '--ref']:
            ref = True
        elif o in ['-M', '--math']:
            math = True
        elif o in ['--debug']:
            debug = True
        else:
            assert False, "Unhandled option %s" % o

    if len(args) == 0:
        show_usage(run=run, short=True)
        sys.exit(0)

    if not outf and not outdir:
        outdir = '-'

    if outf == '-' or outdir == '-':
        outf = False
        outdir = False
    else:
        outdir = outdir or '.'
    if outf and len(args) > 1:
        sys.stderr.write('Argument -o FILE conflicts with multiple files.\n')
        sys.exit(1)

    for f in args:
        if vlev > -2:
            print(f"% Parse {f}")
        lb = ParserMirocDoc(eenv=eenv, etab=etab,
                            label=label, ref=ref, math=math,
                            include=inc,
                            dennou=dennou,
                            verbose=vlev, debug=debug)
        try:
            lb.parse_file(f)
            lb.post_parse_root()
        except Exception as e:
            sys.stderr.write('Panic in %s [%s]\n' % (f, e.args))
            raise

        lb.write(outdir, outf, over=overw)
        if outdir:
            if outf:
                root, ext = os.path.splitext(outf)
                cache = root + '.json'
            else:
                base = os.path.basename(outf or f)
                root, ext = os.path.splitext(base)
                cache = root + '.json'
                cache = os.path.join(outdir, cache)
            cf = open(cache, 'w')
            if vlev > -2:
                print(f'% Create cache {cache}')
            lb.dump(cf)
            cf.close()

        if vlev > 0:
            lb.diag(dump=(vlev > 2),
                    tree=(vlev > 3),
                    tables=(vlev > 1))
    pass


if __name__ == '__main__':
    main(sys.argv[1:], run=sys.argv[0])
    pass
