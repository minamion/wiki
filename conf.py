# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '海蛞蝓杂货铺&罗德岛工程部-Wiki'
copyright = '2023, 盐渍海蛞蝓'
author = '盐渍海蛞蝓'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    "sphinx-favicon",
    'sphinx_design'
    ]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = []
pygments_style = "vs"
pygments_dark_style = "monokai"
language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_baseurl = 'https://wiki.seaslug.moe/'
html_theme = "shibuya"
html_static_path = ['_static']
html_logo = "_static/SeaSlug.png"
html_theme_options = {
    "nav_links": [
        {
            "title": "Blog",
            "url": "https://seaslug.moe"
        },
        {
            "title": "Github",
            "url": "https://seaslug.moe"
        },
        {
            "title": "Oshwhub-个人项目",
            "url": "https://https://oshwhub.com/minamion/"
        },
        {
            "title": "Oshwhub-社团项目",
            "url": "https://oshwhub.com/Rhode-Eng-Dep/"
        },
        {
            "title": "购买链接",
            "url": "https://oshwhub.com/Rhode-Eng-Dep/"
        },
    ],
    "globaltoc_expand_depth": 1,
    "light_css_variables": {
      "--sy-rc-theme": "159, 197, 232",
    },
    "dark_css_variables": {
      "--sy-rc-theme": "130, 80, 223",
    },
    "github_url": "https://github.com/minamion"
}