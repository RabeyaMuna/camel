#!/bin/sh
'''exec' '/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/d2fc7ed0a8fbbc659c3bc88ed1a352815a3c3e71/testbed/.venv-camel-410/bin/python3' "$0" "$@"
' '''

# $Id: rst2odt.py 8994 2022-01-29 16:28:17Z milde $
# Author: Dave Kuhlman <dkuhlman@rexx.com>
# Copyright: This module has been placed in the public domain.

"""
A front end to the Docutils Publisher, producing OpenOffice documents.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline_to_binary, default_description
from docutils.writers.odf_odt import Writer, Reader


description = ('Generates OpenDocument/OpenOffice/ODF documents from '
               'standalone reStructuredText sources.  ' + default_description)


writer = Writer()
reader = Reader()
output = publish_cmdline_to_binary(reader=reader, writer=writer,
                                   description=description)
