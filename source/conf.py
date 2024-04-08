# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import time

sys.path.append(os.path.abspath("tools/extensions"))
sys.path.append(os.path.abspath("includes"))

project = "Madoc"
copyright = f'2024-{time.strftime("%Y")}, Jouron Laurent'
author = "Jouron Laurent"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "notfound.extension",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinxext.opengraph",
]

# The master toctree document.
master_doc = "index"

templates_path = ["_templates"]
exclude_patterns = []

language = "fr"

nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/python/devguide",
    "source_branch": "main",
}
html_static_path = ["_static"]
html_css_files = [
    "devguide_overrides.css",
]
html_js_files = [
    "activate_tab.js",
]
html_logo = "_static/ikigai-cercle.png"
html_favicon = "_static/favicon.png"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "diataxis": ("https://diataxis.fr/", None),
}

todo_include_todos = True

# sphinx-notfound-page
notfound_urls_prefix = "/"

# sphinx.ext.extlinks
# This config is a dictionary of external sites,
# mapping unique short aliases to a base URL and a prefix.
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
extlinks = {
    "github": ("https://github.com/%s/", "%s"),
}

ogp_site_name = "Madoc"
ogp_image = "_static/ikigai-cercle.png"
ogp_custom_meta_tags = [
    '<meta property="og:image:width" content="200">',
    '<meta property="og:image:height" content="200">',
    '<meta name="theme-color" content="#3776ab">',
]

# Strip the dollar prompt when copying code
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#strip-and-configure-input-prompts-for-code-cells
copybutton_prompt_text = "$ "

# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#honor-line-continuation-characters-when-copying-multline-snippets
copybutton_line_continuation_character = "\\"
