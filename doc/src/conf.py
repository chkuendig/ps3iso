# http://www.sphinx-doc.org/en/master/config
import os
import sys

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'PS3ISO'
copyright = '2019, Joshua Stover'
author = 'Joshua Stover'


# -- General configuration ---------------------------------------------------

master_doc = 'index'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.apidoc',
    'sphinxcontrib.autoprogram',
    'generate_history',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Add any paths that contain custom static files (such as style sheets) here,
html_static_path = ['_static']

# Source file/directory patterns to ignore. Relative to source directory
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
html_theme = 'nature'


# -- Apidoc setup ------------------------------------------------------------

apidoc_module_dir = '../../ps3iso'
apidoc_output_dir = 'apidoc'
apidoc_excluded_paths = ['']
apidoc_separate_modules = False
apidoc_toc_file = False
apidoc_module_first = True

