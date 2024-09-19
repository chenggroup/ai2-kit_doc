# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ai2-kit'
copyright = '2024, weihong.xu'
author = 'weihong.xu'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    "nbsphinx",
    'sphinxcontrib.bibtex',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    #'autoapi.extension',
    'sphinxcontrib.autodoc_pydantic'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'ai2-kit']

bibtex_bibfiles = ['references.bib']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "show_toc_level": 2,
    "secondary_sidebar_items": ["page-toc", "sourcelink"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/chenggroup/ai2-kit",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/ai2-kit",
            "icon": "fa-brands fa-python",
        },
        {
            "name": "AI4EC",
            "url": "https://ai4ec.ikkem.com",
            "icon": "fa-solid fa-globe",
        },
    ],
}
html_static_path = ['_static']
nbsphinx_execute = 'never'

autosummary_generate = True

repository = 'https://github.com/chenggroup/ai2-kit'
