#!/bin/sh
'''exec' '/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/d2fc7ed0a8fbbc659c3bc88ed1a352815a3c3e71/testbed/.venv-camel-410/bin/python3' "$0" "$@"
' '''

# $Id: rst2xetex.py 8956 2022-01-20 10:11:44Z milde $
# Author: Guenter Milde
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Lua/XeLaTeX code.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline

description = ('Generates LaTeX documents from standalone reStructuredText '
               'sources for compilation with the Unicode-aware TeX variants '
               'XeLaTeX or LuaLaTeX. '
               'Reads from <source> (default is stdin) and writes to '
               '<destination> (default is stdout).  See '
               '<https://docutils.sourceforge.io/docs/user/latex.html> for '
               'the full reference.')

publish_cmdline(writer_name='xetex', description=description)
