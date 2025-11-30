# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Suzauku"
copyright = "2025, XiangQinxi"
author = "XiangQinxi"
release = "0.1.9"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_inline_tabs",
    "myst_parser",  # Markdown parser
    "sphinx.ext.ifconfig",
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
]

# 指定 graphviz 输出格式（推荐 SVG 或 PNG）
graphviz_output_format = 'svg'


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

languages = {
    'zh_CN': '中文(简体)',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
