# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from acanban import __version__

# Project information
project = 'Acanban'
copyright = '2020  Ngô Ngọc Đức Huy et al.'  # noqa
author = 'Ngô Ngọc Đức Huy et al.'
release = __version__

# Add any Sphinx extension module names here, as strings.
# They can be extensions coming with Sphinx (named 'sphinx.ext.*')
# or your custom ones.
extensions = ['sphinx.ext.extlinks', 'sphinx.ext.githubpages',
              'sphinxcontrib.plantuml']
extlinks = {'doi': ('https://doi.org/%s', 'doi: ')}
plantuml_output_format = 'svg_img'
plantuml_latex_output_format = 'pdf'

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match
# files and directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Options for HTML output
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory.  They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = []

# Options for LaTeX
latex_elements = {
    'papersize': 'a4paper', 'pointsize': '12pt',
    'fontpkg': r'\usepackage{lmodern}',
    'babel': r'\usepackage[english,vietnamese]{babel}',
    'tableofcontents': r'\selectlanguage{english}\sphinxtableofcontents'}
