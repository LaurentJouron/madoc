.. _intersection:

============
Intersection
============

L'algorithme de la sécante est une méthode numérique utilisée pour trouver les intersections d'une 
fonction avec l'axe des x, c'est-à-dire les points où la fonction coupe l'axe des x.
Pour ce faire, l'algorithme utilise deux points de départ initiaux, x0 et x1, et calcule une approximation 
de la racine de la fonction en utilisant une formule basée sur la pente de la sécante entre ces deux points. 
Ensuite, il répète ce processus en utilisant le nouveau point calculé jusqu'à ce qu'une précision suffisante 
soit atteinte.

Dans notre implémentation, la fonction intersection prend en paramètres la fonction dont nous voulons trouver 
la racine, ainsi que deux points de départ initiaux, initial_guess1 et initial_guess2. L'algorithme utilise ces 
points pour calculer progressivement une meilleure approximation de la racine en utilisant la méthode de la sécante. 
La boucle while True est utilisée pour itérer jusqu'à ce que la différence entre deux approximations successives 
soit inférieure à un seuil de précision défini.

La fonction f(x) est la fonction dont nous voulons trouver la racine, dans cet exemple, f(x) = x^3 - 2x - 5.

Enfin, l'algorithme renvoie la valeur de la racine calculée avec une précision suffisante.

Fonction
--------

.. code-block:: Python

    import math

    def intersection(function, initial_guess1, initial_guess2):
        """
        Finds the intersection of the function with the x-axis using the secant method.

        Args:
            function: The function for which to find the root.
            initial_guess1: The first initial guess.
            initial_guess2: The second initial guess.

        Returns:
            The root of the function.
        """
        x_n = initial_guess1
        x_n1 = initial_guess2

        while True:
            x_n2 = x_n1 - (function(x_n1) / ((function(x_n1) - function(x_n)) / (x_n1 - x_n)))
            if abs(x_n2 - x_n1) < 10**-5:
                return x_n2
            x_n = x_n1
            x_n1 = x_n2

    def f(x):
        """
        The function f(x) = x^3 - 2x - 5.

        Args:
            x: The input value.

        Returns:
            The result of the function.
        """
        return math.pow(x, 3) - (2 * x) - 5


Utilisation
-----------

.. code-block:: Python

    print(intersection(f, 3, 3.5))


Resultats
---------

.. code-block:: Python

    2.0945514815435184

.. note::

    .. raw:: html

        Auteur: <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a>