#!/usr/bin/env python3
# Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>
# 'Time-stamp: <2020/07/20 09:09:53 fuyuki evacuate.py>'

# import psitex as psi
import psitex
import sys
import getopt
import os.path
import string
import re
import copy
import pprint as ppr
import pyparsing as pp


class ParserMirocDoc(psitex.ParserBase, psitex.ParserStd):
    """Simple class for MIROC document replacement."""

    def __init__(self, macros=None,
                 eenv=None, etab=None, dennou=False, **kw):
        """Initialize MIROC-Doc replacement."""
        macros = macros or {}
        macros['Module'] = 1
        macros['Dvect'] = 1
        macros['DP'] = (4, 1, 2)
        macros['DD'] = (3, 1)

        super().__init__(macros=macros, **kw)

        self.dennou = dennou
        self.tbl_imath = {}
        self.tbl_emath = {}
        self.tabular = {}
        self.fmt_imath = 'TERM%05d'
        self.fmt_emath = 'EQ=%05d.'
        self.fmt_tabular = 'TAB%05d:'

        self.cache.update(imath=self.tbl_imath,
                          emath=self.tbl_emath)
        if eenv == 'q':
            eenv = 'quote'
        elif eenv in ['qn', 'qq']:
            eenv = 'quotation'
        if eenv not in [None, 'quote', 'quotation']:
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

        pass

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
        tmpl = r'\mbox{{\boldmath ${}$}}'.format(a)
        toks = self.parse_string(tmpl)
        return(toks)

    def post_parse(self, *args, **kw):
        """Batch replacement of special macros."""
        super().post_parse(*args, **kw)
        self.rep_module()
        self.rep_imath()
        self.rep_enveq()
        self.rep_envar()
        self.rep_dispm()
        self.rep_tabular()

    def rep_module(self, tree=None):
        r"""Replace \Module macros."""
        tree = tree or self.tree
        for m in self.search(tree, r'\Module'):
            a = m.P['#1']['C']
            arep = [r'MODULE:[', *a, ']']
            self.modify_macro(m, macro=r'\texttt', args=[(1, arep)])

    def rep_imath(self, tree=None, fmt=None, lev=0):
        """Replace inline maths."""
        strsep = string.punctuation + string.whitespace

        tree = tree or self.tree
        fmt = fmt or self.fmt_imath
        math = False
        rsfx = re.compile('[a-zA-Z]+$')
        rpfx = re.compile(r'^[a-zA-Z]+')

        for j, a in enumerate(tree):
            if math:
                p, m = tree[j-2:j]
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
                        sys.stdout.write('unit/chem mode (%s:%s:%s)\n'
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
        tree = tree or self.tree
        for m in self.search_env(tree, r'equation', r'equation*',
                                 r'displaymath', ):
            lbl = self.search(m, r'\label')
            txt = fmt % len(self.tbl_emath)
            src = m.B.copy()
            self.tbl_emath[txt] = src
            rep = [txt, '\n']
            if len(lbl) == 1:
                rep.extend([lbl, '\n'])
            elif len(lbl) > 1:
                ll = [''.join(psi.flatten(li)) for li in lbl]
                sys.stderr.write('Multiple labels {%s}\n' % ' '.join(ll))
            self.modify_env(m, body=rep)
            if self.eenv:
                self.modify_env(m, name=self.eenv)

    def rep_envar(self, tree=None, fmt=None):
        """Replace eqnarray environement."""
        fmt = fmt or self.fmt_emath
        tree = tree or self.tree
        for m in self.search_env(tree, r'eqnarray', r'eqnarray*'):
            txt = fmt % len(self.tbl_emath)
            src = m.B.copy()
            self.tbl_emath[txt] = src
            rep = []
            for a in m.B.asList():
                if a == '\\\\':
                    rep.extend([txt, a, '\n'])
                elif a == '':
                    pass
                elif a[0] == r'\label':
                    rep.append(a)
                    rep.append('\n')
                elif a == r'\nonumber':
                    rep.append(a)
                    rep.append('\n')
            rep.extend([txt, '\n'])
            self.modify_env(m, body=rep)
            if self.eenv:
                self.modify_env(m, name=self.eenv)

    def rep_dispm(self, tree=None, fmt=None):
        r"""Replace displaymath (\[\])."""
        fmt = fmt or self.fmt_emath
        tree = tree or self.tree

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
                sys.stderr.write('Ignore displaymath %s\n' % chk)

    def rep_tabular(self, tree=None, fmt=None):
        """Replace tabular environement."""
        if self.etab is None:
            return
        if self.etab != 'description':
            return

        fmt = fmt or self.fmt_tabular
        self.cache['tabular'] = self.tabular

        tree = tree or self.tree
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
                        rep.append([r'\item',
                                    ['[', label, ']'], ' '] + e + ['\n'])
            self.modify_env(m, body=rep, name=self.etab, args=None)
            # m[2] = []

    def diag(self, *args, **kw):
        """Diagnostic."""
        super().diag(*args, **kw)
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


def main(args, run):
    """Main."""
    try:
        opts, args = getopt.getopt(args, 'vqfc:o:d:E:T:D',
                                   ['verbose', 'quiet', 'debug',
                                    'force',
                                    'cache=', 'output=','outdir=',
                                    'dennou',
                                    'equation=', ])
    except getopt.GetoptError as err:
        print(err)
        raise
    debug = False
    cachedir = None
    outdir = None
    outf = None
    overw = False
    vlev = 0
    eenv = None
    etab = None
    dennou = None
    for o, a in opts:
        if o in ['-c', '--cache']:
            cachedir = a
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
        elif o in ['--debug']:
            debug = True
    if len(args) > 1 and outf:
        if outf == '-':
            pass
        elif os.path.isdir(outf):
            outdir = outf
            outf = None
        else:
            sys.stderr.write("Need output directory, not a file name %s\n"
                             % outf)
            sys.exit(1)
    if len(args) > 1:
        outdir = outdir or '.'
        if outf and outf != '-':
            sys.stderr.write("Cannot apply file name %s\n" % outf)
            sys.exit(1)
    elif len(args) == 1:
        if outf and outf != '-':
            if os.path.isdir(outf):
                outdir = outdir or outf
                outf = None
        else:
            outdir = outdir or '.'

    cachedir = cachedir or outdir or '.'
    for f in args:
        # tree, imath, emath, envs = gen_tree(r.asList())
        base = os.path.basename(f)
        root, ext = os.path.splitext(base)
        if outdir == '-' or outf == '-':
            tex = 'stdout'
            of = None
        else:
            tex = outf or os.path.join(outdir, base)
            if os.path.exists(tex) and not overw:
                sys.stderr.write('Exists %s, skipped.\n' % tex)
                continue
            of = open(tex, 'w')
        if cachedir == '-':
            cache = 'stdout'
            cf = None
        else:
            cache = root + '.json'
            cache = os.path.join(cachedir, cache)
            cf = open(cache, 'w')

        print("# %s > %s [%s]" % (f, tex, cache))
        lb = ParserMirocDoc(eenv=eenv, etab=etab,
                            dennou=dennou, debug=debug)
        try:
            lb.parse_file(f)
        except Exception as e:
            sys.stderr.write('Panic in %s [%s]\n' % (f, e.args))
            raise

        lb.write(of)
        lb.dump(cf)

        if of:
            of.close()
        if cf:
            cf.close()

        if vlev > 0:
            lb.diag(dump=(vlev > 1))
    pass


if __name__ == '__main__':
    main(sys.argv[1:], run=sys.argv[0])
    pass
