.. _numpy_scipy:

===========
Numpy/Scipy
===========

Style NumPy/Scipy
-----------------

.. image:: https://img.shields.io/badge/docstrings-numpy/scipy-blue.svg?style=for-the-badge&logo=python&logoColor=white
   :alt: NumPy/SciPy Docstrings Badge
   :target: https://numpydoc.readthedocs.io/en/latest/format.html

Ce style est similaire au style :doc:`Google <google>`, mais utilise des sections spécifiques pour décrire les paramètres, les valeurs de retour, etc.

⚙️ NumPy/SciPy

.. code-block:: Python

    def multiply_matrix(matrix, scalar):
        """
        Multiply a matrix by a scalar.

        Parameters
        ----------
        matrix : numpy.ndarray
            The input matrix to be multiplied.
        scalar : int or float
            The scalar value to multiply the matrix by.

        Returns
        -------
        numpy.ndarray
            The resulting matrix after multiplication.
        """
        return matrix * scalar

Affiche les docstrings
----------------------

.. code-block:: Python

    print(multiply_matrix.__doc__)


Resultats
---------

.. code-block:: Python

    Multiply a matrix by a scalar.

    Parameters
    ----------
    matrix : numpy.ndarray
        The input matrix to be multiplied.
    scalar : int or float
        The scalar value to multiply the matrix by.

    Returns
    -------
    numpy.ndarray
        The resulting matrix after multiplication. 