#!/bin/sh
'''exec' '/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/d2fc7ed0a8fbbc659c3bc88ed1a352815a3c3e71/testbed/.venv-camel-410/bin/python3' "$0" "$@"
' '''

# $Id: rst2html4.py 8927 2022-01-03 23:50:05Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing (X)HTML.

The output conforms to XHTML 1.0 transitional
and almost to HTML 4.01 transitional (except for closing empty tags).
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='html4', description=description)
