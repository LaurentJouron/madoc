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
copyright = f'2024-{time.strftime("%Y")}, Laurent Jouron'
author = "Laurent Jouron"

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

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "venv*",
    "env*",
    "README.rst",
    ".github",
]

language = "fr"

nitpicky = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/LaurentJouron/madoc",
    "source_directory": "docs/",
    "source_branch": "main/source",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_button": None,
    "light_css_variables": {
        "color-brand-primary": "#bf1e2e",
        "color-brand-content": "#bf1e2e",
        "font-stack": "Verdana, Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/LaurentJouron/madoc",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

html_static_path = ["_static"]
html_css_files = [
    "devguide_overrides.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_js_files = [
    "activate_tab.js",
]
html_logo = "_static/ikigai-cercle.png"
html_favicon = "_static/ikigai-cercle.png"
html_title = "Madoc"

pygments_style = "sphinx"
pygments_dark_style = "monokai"

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

# sphinxext-opengraph config
ogp_site_url = "https://laurentjouron.github.io/"
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
