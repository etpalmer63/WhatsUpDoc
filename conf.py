# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'WhatsUpDoc'
copyright = '2021, Erik Palmer'
author = 'Erik Palmer'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']



#time date format
from time import gmtime, strftime, localtime
today = strftime("%a, %d %b %Y %H:%M:%S", localtime())
#today = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

#make time badge
from pybadges import badge
doc_time_badge = badge(left_text='Doc Change:', right_text=today, left_color='blue')
#write svg out as file
with open('doc_time_badge.svg', 'w') as f:
    f.write(doc_time_badge)
f.close()


import importlib.util
spec = importlib.util.spec_from_file_location("git_file_last_changed_date", "/home/erik/FastStorage/WhatsUpDoc/git_file_last_changed_date.py")
codechangedate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(codechangedate)



code_time_badge = badge(left_text='Code Change:', right_text=codechangedate.find_last_change(), left_color='green')
with open('code_time_badge.svg', 'w') as f:
    f.write(code_time_badge)
f.close()

