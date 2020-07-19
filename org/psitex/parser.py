#!/usr/bin/env python3
# Maintainer: SAITO Fuyuki <saitofuyuki@jamstec.go.jp>
# 'Time-stamp: <2020/07/17 09:26:22 fuyuki parser.py>'

import sys
import psitex.lexer

class ParserBase(psitex.lexer.LexerBase):
    """Simple class for LaTeX parser."""

    def post_parse(self, *args, **kw):
        """Batch replacement of special macros."""
        super().post_parse(*args, **kw)
        self.tree = self.orig.copy()
        self.cache['orig'] = self.cache['tree']
        self.cache['tree'] = self.tree

    def write(self, file=None, tree=None):
        """Write results to file."""
        file = file or sys.stdout
        if tree is None:
            tree = self.tree
        elif tree is False:
            tree = self.orig
        file.write(''.join(self.flatten(tree)))


def main(args, run):
    """Main."""
    psitex.lexer.main(args, run)
    pass


if __name__ == '__main__':
    main(sys.argv[1:], run=sys.argv[0])
    pass
