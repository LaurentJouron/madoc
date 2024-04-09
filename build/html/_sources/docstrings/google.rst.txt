.. _google:

======
Google
======

.. image:: https://img.shields.io/badge/docstrings-google-blue.svg?style=for-the-badge&logo=google&logoColor=white
   :alt: Google Docstrings Badge
   :target: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Style Google
------------

Rien n'empêche d'écrire les docs en français, mais il est préférable de les écrire en anglais, afin de respecter les conventions de la pep8.

⚙️ Google

.. code-block:: Python

        def addition(a, b):
            """
            This function takes two numbers as input and returns their sum.

            Args:
                a (int): The first number.
                b (int): The second number.

            Returns:
                int: The sum of the two numbers.
            """
            return a + b


Affiche les docstrings
----------------------

Pour affcicher la docstring d’une fonction, classe ou méthode, il est suffit d’écrire le nom de celle-ci, suivi de ``.__doc__``.

.. code-block:: Python

        print(addition.__doc__)

Resultats
---------

.. code-block:: Python

        This function takes two numbers as input and returns their sum.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of the two numbers.