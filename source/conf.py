# -*- coding: utf-8 -*-
#
# OpenDataHub Docs documentation build configuration file, created by
# sphinx-quickstart on Mon Apr 30 16:18:05 2018.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import io
import time
current_year = time.strftime('%Y')
sys.path.append(os.path.abspath("./_ext"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
#needs_sphinx = '2.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx.ext.imgconverter',
    'ga', 'hidemail',
    'sphinx_togglebutton', 'sphinx_panels',
    'sphinx_copybutton', 'changelog'
]

### Configuration values for extensions

togglebutton_hint = "More..."

copybutton_prompt_text = r'\~\$ |\~\# '
copybutton_prompt_is_regexp = True


# section names - we don't need them 
#changelog_sections = ["Improvements", "Changes", "Bugfix"]

# tags to sort on inside of sections
changelog_inner_tag_sort = ["Improvement", "Change", "Bugfix", "New Feature"]
# whether sections should be hidden from tags list
#changelog_hide_sections_from_tags = False
changelog_render_ticket = "https://github.com/noi-techpark/odh-docs/issues/%s"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'OpenDataHub Docs'
copyright = u'2018-%s, The ODH Team' %(current_year)
author = u'The ODH Team'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'2021.08'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [ 'replace.rst', 'dtp.rst', 'datasets',
                     'domains.rst', 'architecture.rst',
                     'howto/tourism/access.rst', 'includes', 'kg.rst' ] 

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

rst_prolog = """

.. role:: license
.. role:: green
.. role:: uline
.. role:: button
.. role:: monospace
.. role:: greenswbutton 
.. role:: raw-latex(raw)
   :format: latex 
.. role:: strike
""" + open("replace.rst").read()

# facility to shorten/change external links - useful if hosting changes
#
# IMPORTANT! not all links can be shortened (i.e., when they are
# within example GET calls), so make sure to fix those as well.

extlinks = { 'sasabus': ('http://sasabus.org/%s', None),
             'stinfo':
             ('https://tourism.api.opendatahub.bz.it/#%s', None),
             'apit':
             ('https://tourism.api.opendatahub.bz.it/v1%s', None)
}

numfig = True
numfig_format = { 'figure': ('Figure %s'),
                  'table': ('Table %s'),
                  'code-block': ('Listing %s'),
                  'section': ('Section')
}

# fontawesome css, required by sphix-panels
panels_add_fontawesome_latex = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'odh'

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['.']

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
html_title = u'OpenDataHub Docs Repo'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
html_logo = 'images/OpenDataHub.png'

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = ''

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
html_use_smartypants = True

# If false, no index is generated.
#
html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_copy_source = False
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = False

googleanalytics_id = 'UA-138331709-2'

# Output file base name for HTML help builder.
htmlhelp_basename = 'OpenDataHubDocsdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     'preamble': r'\usepackage{odh}',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'OpenDataHubDocs.tex', u'OpenDataHub Docs Documentation',
     u'The Open Data Hub Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
latex_logo = 'images/OpenDataHub.png'

latex_additional_files = [ 'odh.sty' ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'opendatahubdocs', u'OpenDataHub Docs Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False

# -- Options for linkcheck output -------------------------------------------

linkcheck_anchors = False
linkcheck_retries = 2
linkcheck_ignore = [
    'https://ci.opendatahub.bz.it',
    'https://github.com/your-username/',
    'http://localhost:\d+/',
    'https://cert.provinz.bz.it/musport/services/MuseumsService.MuseumsServiceHttpSoap11Endpoint/',
    'http://tourism.opendatahub.bz.it/token'
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'OpenDataHubDocs', u'OpenDataHub Docs Documentation',
     author, 'OpenDataHubDocs', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
epub_css_files = [ 'odh.css' ]

def setup(app):
    app.add_css_file('https://use.fontawesome.com/releases/v5.7.0/css/all.css')
    app.add_js_file('searchtools.js')
    app.add_config_value('googleanalytics_id', '', 'html')
    app.add_config_value('googleanalytics_enabled', True, 'html')
