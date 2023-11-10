# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AGGRESSOR NETWORK USER MANUAL'
copyright = '2023, bitset'
author = 'Inc. bitset'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.todo',
]

[extensions]
todo_include_todos=True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'
numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']

html_show_sourcelink = False

# -- Options for LaTeX output ------------------------------------------------
#
#latex_docclass = {'manual': 'jsbook'}
#latex_documents = [
#    ('index', 'archbook.tex', project, author, 'manual', True),
#]

latex_elements = {
    'papersize': 'a4paper',
    'extraclassoptions': 'openany',
    #'preamble': '\n'.join([
    #  r'\setlength{\parindent}{1zw}',
    #  r'\setlength{\parskip}{0ex}',
      #r'\usepackage{\fancyhdr}',
      #r'\pagestyle{\fancy}',
      #r'\fancyhf{}',
      #r'\rfoot{\thepage}',
      #r'\fancyfoot[C]{\thepagee}',
    #]),
    'preamble': r'''
    \usepackage{fancyhdr} 
    \pagestyle{fancy} 
    \fancyhf{} 
    \rfoot{\thepage} 
    \fancyfoot[C]{\thepagee} 
    '''

}



latex_logo = '_static/logo_aggressor_network_256.png'
