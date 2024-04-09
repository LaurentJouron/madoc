==========
Bissection
==========

L'algorithme de la bissection est une méthode numérique utilisée pour trouver les racines d'une 
fonction continue sur un intervalle donné. L'objectif est de déterminer un intervalle où la fonction 
change de signe, ce qui indique la présence d'une racine à l'intérieur de cet intervalle. Ensuite, 
l'algorithme divise cet intervalle en deux parties égales et évalue la fonction au point médian. En 
fonction du signe du résultat, l'algorithme choisit le sous-intervalle contenant la racine et répète 
le processus jusqu'à ce qu'une précision suffisante soit atteinte. Cette méthode est particulièrement 
utile pour les fonctions continues mais peut nécessiter un nombre important d'itérations pour atteindre 
la précision souhaitée.

.. code-block:: Python

    import math

    def bisection(function, start_interval, end_interval):
        """
        Finds where the function becomes 0 in [start_interval, end_interval] using the bisection method.

        Args:
            function: The function for which to find the root.
            start_interval: The start of the interval.
            end_interval: The end of the interval.

        Returns:
            The root of the function within the given interval.
        """
        start = start_interval
        end = end_interval

        if function(start_interval) == 0:
            return start_interval
        elif function(end_interval) == 0:
            return end_interval
        elif function(start_interval) * function(end_interval) > 0:
            print("Couldn't find root in [start_interval, end_interval]")
            return
        else:
            mid = (start + end) / 2
            while abs(start - mid) > 10**-7:
                if function(mid) == 0:
                    return mid
                elif function(mid) * function(start) < 0:
                    end = mid
                else:
                    start = mid
                mid = (start + end) / 2
            return mid

    def f(x):
        """
        The function f(x) = x^3 - 2x - 5.

        Args:
            x: The input value.

        Returns:
            The result of the function.
        """
        return math.pow(x, 3) - 2*x - 5

    print(bisection(f, 1, 1000))
