#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from misc.cyverse_sphinx_conf import *  # noqa

project = 'GenoPhenoEnvo'
copyright = '2020, University of Arizona'
author = 'TL Swetnam'
version = '0.0.1'
release = '0.0.1'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# html theme configuration -- see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme_options = {
    'display_version': False,
    # Table of Content options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']
