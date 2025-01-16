import os
import sys

# Ajouter les chemins nécessaires pour inclure les fichiers Python dans la documentation
sys.path.insert(0, os.path.abspath('../src'))  # Modifier selon votre structure
sys.path.insert(0, os.path.abspath('.'))      # Inclure le répertoire courant si nécessaire

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SysWatch'
copyright = '2025, romain, amandine, lucas'
author = 'romain, amandine, lucas'
release = '1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
