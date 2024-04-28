.. _newton_method:

=============
Newton method
=============

La fonction newton_method applique la méthode de Newton pour trouver la racine d'une fonction donnée. 
Cette méthode, également connue sous le nom de méthode de la tangente, utilise les informations de la fonction 
et de sa dérivée pour approximer la racine.

La fonction prend trois paramètres en entrée : function, qui est la fonction dont nous voulons trouver la 
racine, derivative_function, qui est la dérivée de cette fonction, et starting_point, qui est le point de 
départ initial pour l'approximation de la racine.

En utilisant la formule de la méthode de Newton, l'algorithme itère jusqu'à ce que la différence entre deux 
approximations successives soit inférieure à un seuil de précision défini. Une fois que la condition de 
convergence est atteinte, l'algorithme renvoie la valeur approximative de la racine.

Dans notre exemple, nous utilisons la fonction f(x) = x^3 - 2x - 5 et sa dérivée f1(x) = 3x^2 - 2. En appliquant 
la méthode de Newton avec ces fonctions et un point de départ initial de 3, nous obtenons une approximation 
de la racine de la fonction.

Cette méthode est largement utilisée en optimisation numérique et en analyse numérique pour résoudre des 
équations non linéaires et trouver des points critiques de fonctions.

Fonction
--------

.. code-block:: Python
    :emphasize-lines: 1,23,27
    :linenos:

    def newton_method(function, derivative_function, starting_point):
        """
        Applies Newton's method to find the root of a function.

        Args:
            function: The function for which to find the root.
            derivative_function: The derivative of the function.
            starting_point: The initial guess for the root.

        Returns:
            The approximated root of the function.
        """
        x_n = starting_point
        
        while True:
            x_n1 = x_n - function(x_n) / derivative_function(x_n)
            
            if abs(x_n - x_n1) < 10 ** -5:
                return x_n1
            
            x_n = x_n1

    def f(x):
        """The function f(x) = x^3 - 2x - 5."""
        return x ** 3 - 2 * x - 5

    def f1(x):
        """The derivative of f(x)."""
        return 3 * x ** 2 - 2

.. tab:: Utilisation
    
    .. code-block:: Python
        :emphasize-lines: 1

        root = newton_method(f, f1, 3)
        print(f"Approximated root: {root}")

.. tab:: Resultats

    .. code-block:: Python

        Approximated root: 2.0945514815423474

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>