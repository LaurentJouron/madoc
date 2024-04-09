==========
Docstrings
==========

.. important::

    .. image:: https://img.shields.io/badge/docstrings-google-blue.svg?style=for-the-badge&logo=google&logoColor=white
        :alt: Google Docstrings Badge
        :target: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

    .. image:: https://img.shields.io/badge/docstrings-numpy/scipy-blue.svg?style=for-the-badge&logo=python&logoColor=white
        :alt: NumPy/SciPy Docstrings Badge
        :target: https://numpydoc.readthedocs.io/en/latest/format.html

    .. image:: https://img.shields.io/badge/sphinx-%23C4302B.svg?style=for-the-badge&logo=sphinx&logoColor=white
        :alt: Sphinx Badge
        :target: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html


    Pour voir la **documentation officielle** cliquez sur les badges. Je rappelle que ce sont des notes personnelles que je mets à disposition.
    Ces notes ne se substituent au aucun moment à la documentation officielle de `google <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_ ou 
    `numpy/scipy <https://numpydoc.readthedocs.io/en/latest/format.html>`_. Il y a de belles explications sur `Sphinx <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.

Qu'est ce que les docstrings
----------------------------

💡 Les docstrings Python sont des chaînes de documentation qui sont incorporées directement dans le code source d’une fonction, 
d’une classe ou d’un module. Ils sont utilisés pour fournir des informations claires et concises sur le but auquel ils sont associés. 
Les docstrings sont accessibles via l’attribut _doc_ de l’objet concerné et sont utilisés pour générer automatiquement une 
documentation plus détaillée à l’aide d’outils tels que Sphinx.

Ces styles docstring permettent aux développeurs de comprendre rapidement comment utiliser une fonction ou une classe sans avoir 
à examiner le code source, ce qui facilite la collaboration et la maintenance du code.

Il existe plusieurs styles de docstrings en Python, mais deux des plus courants sont:

.. toctree::
   :maxdepth: 3

   google
   numpy_scipy