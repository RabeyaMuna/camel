#!/bin/sh
'''exec' '/home/yisenxu/rabeya/mini-swe-agent-ci-based/results/think_repair_deepseek/e1dbd83b5eccd0a5435563900d30381bb4d4f27a/testbed/.venv-camel-415/bin/python' "$0" "$@"
' '''

# Author:
# Contact: grubert@users.sf.net
# Copyright: This module has been placed in the public domain.

"""
man.py
======

This module provides a simple command line interface that uses the
man page writer to output from ReStructuredText source.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description
from docutils.writers import manpage

description = ("Generates plain unix manual documents.  "
               + default_description)

publish_cmdline(writer=manpage.Writer(), description=description)
