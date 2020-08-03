# -*- coding: utf-8 -*-

import sys
import os
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

extensions = [
    'sphinx.ext.autodoc',
]

project = 'Geno-Pheno-Envo'
copyright = '2020, University of Arizona'
author = 'Tyson L Swetnam'
version = '0.0.1'
release = '0.0.1'

language = None
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst']

common_static_path = os.path.join(os.path.dirname(__file__), 'static')

templates_path = ['_templates']
html_static_path = ['_static', common_static_path]
exclude_patterns = ['_build']
master_doc = 'index'
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'

htmlhelp_basename = 'GenoPhenoEnvo_Documentation'

latex_elements = {}
latex_documents = [
    (master_doc, 'GenoPhenoEnvoDocumentation.tex', 'GenoPhenoEnvo Documentation',
     'GenoPhenoEnvo', 'manual'),
]

man_pages = [
    (master_doc, 'GenoPhenoEnvo Documentation', 'GenoPhenoEnvo Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'GenoPhenoEnvo Documentation', 'GenoPhenoEnvo Documentation',
     author, 'Tyson Swetnam', 'CyVerse',
     'Miscellaneous'),
]

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']


def setup(app):
    app.add_config_value(
        'recommonmark_config',
        {
            'enable_auto_toc_tree': True,
            'enable_eval_rst': True,
            'auto_toc_tree_section': 'Contents',
        },
        True
    )
    app.add_transform(AutoStructify)
    app.add_stylesheet('cyverse.css')
    app.add_javascript('jquery.tablesorter.min.js')
    app.add_javascript('cyverse.js')
