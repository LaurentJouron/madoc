.. _lu_decomposition:

================
Lu decomposition
================

La fonction lu_decompose réalise la décomposition LU d'une matrice carrée en une matrice triangulaire 
inférieure (L) et une matrice triangulaire supérieure (U) en utilisant la méthode de décomposition LU. 
Cette méthode est couramment utilisée en algèbre linéaire pour résoudre des systèmes d'équations linéaires 
et inverser des matrices.

La fonction prend en paramètre une matrice carrée et retourne les matrices L et U. Elle itère sur les 
éléments de la matrice d'entrée pour calculer les éléments des matrices L et U en suivant un processus 
spécifique. Les résultats obtenus sont ensuite retournés sous forme de tuples contenant les matrices L et U.

En utilisant cette fonction, les utilisateurs peuvent facilement décomposer une matrice carrée en ses 
composantes L et U, ce qui peut être utile dans de nombreuses applications en mathématiques, en science 
des données et en ingénierie.

Fonction
--------

.. code-block:: Python

    import numpy

    def lu_decompose(matrix):
        """
        Decomposes a square matrix into its lower triangular matrix (L) and upper triangular matrix (U) using LU decomposition.

        Args:
            matrix: The square matrix to be decomposed.

        Returns:
            L: The lower triangular matrix.
            U: The upper triangular matrix.
        """
        rows, columns = numpy.shape(matrix)
        L = numpy.zeros((rows, columns))
        U = numpy.zeros((rows, columns))

        if rows != columns:
            return []

        for i in range(columns):
            for j in range(i):
                sum = 0
                for k in range(j):
                    sum += L[i][k] * U[k][j]
                L[i][j] = (matrix[i][j] - sum) / U[j][j]
            
            L[i][i] = 1
            
            for j in range(i, columns):
                sum1 = 0
                for k in range(i):
                    sum1 += L[i][k] * U[k][j]
                U[i][j] = matrix[i][j] - sum1

        return L, U


Utilisation
-----------

.. code-block:: Python

    matrix = numpy.array([[2, -2, 1],
                        [0, 1, 2],
                        [5, 3, 1]])

    L, U = lu_decompose(matrix)
    print("Lower triangular matrix (L):")
    print(L)
    print("\nUpper triangular matrix (U):")
    print(U)


Resultats
---------

.. code-block:: Python

    Lower triangular matrix (L):
    [[1.  0.  0. ]
    [0.  1.  0. ]
    [2.5 8.  1. ]]

    Upper triangular matrix (U):
    [[  2.   -2.    1. ]
    [  0.    1.    2. ]
    [  0.    0.  -17.5]]