.. _depth_first_search :


==================
Depth-First Search
==================

La recherche en profondeur (Depth-First Search ou DFS en anglais) est un algorithme utilisé pour parcourir ou rechercher des structures de données arborescentes ou de graphe. Contrairement à BFS, DFS explore autant que possible le plus loin le long d'une branche avant de revenir en arrière.

* Commencez par un nœud de départ et empilez-le sur une pile.
* Marquez le nœud de départ comme exploré.
* Tant que la pile n'est pas vide.
    *   Dépilez un nœud de la pile (celui le plus récemment empilé).
    *   Parcourez tous les voisins non explorés de ce nœud.
    *   Pour chaque voisin non exploré, marquez-le comme exploré et empilez-le sur la pile.
* Répétez l'étape 3 jusqu'à ce que la pile soit vide.

* DFS explore autant que possible le plus loin le long d'une branche avant de revenir en arrière. Cela signifie qu'il explore chaque branche aussi loin que possible avant de passer à une autre branche.
* DFS est généralement implémenté à l'aide d'une pile (ou de la récursivité), ce qui signifie qu'il utilise moins de mémoire que BFS pour les graphes très profonds.

Trouver le chemin le plus profond dans un arbre ou un graphe.

Détecter les cycles dans un graphe.

Trouver des solutions à des problèmes de recherche, comme le problème du voyageur de commerce.

Complexité temporelle : O(V + E), où V est le nombre de sommets (nœuds) et E est le nombre d'arêtes dans le graphe.

Complexité spatiale : O(V), où V est le nombre de sommets. Cela est dû à l'utilisation de la pile pour stocker les nœuds à explorer.

.. code-block:: Python

         A
       /   \
      B     C
     / \   / \
    D   E F   G

En partant du nœud A, DFS explorerait la branche de gauche jusqu'au nœud D, puis reviendrait en arrière pour explorer les autres nœuds de cette branche, avant de passer à la branche de droite.

La recherche en profondeur est un algorithme fondamental pour parcourir et rechercher des graphes. Sa capacité à explorer les branches en profondeur le rend utile dans de nombreuses applications, telles que la recherche de solutions de problèmes et la détection de cycles dans les graphes.

Fonction
--------

.. code-block:: Python
    :emphasize-lines: 1,3
    :linenos:

    def dfs(graph, start):
    """
    Perform Depth-First Search (DFS) on a graph starting from a given node.

    Args:
        graph (dict): The graph represented as a dictionary where keys are nodes and values are lists of neighboring nodes.
        start: The starting node for DFS traversal.

    Returns:
        set: A set containing all nodes explored during DFS traversal.
    """
    explored, stack = set(), [start]
    explored.add(start)
    while stack:
        current_node = stack.pop()  # The difference from BFS is popping the last element here instead of the first one
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                explored.add(neighbor)
                stack.append(neighbor)
    return explored


    G = {'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']}


.. tab:: Utilisation
    
    .. code-block:: Python
    
        print(dfs(G, 'A'))

.. tab:: Resultats

    .. code-block:: shell

        {'D', 'E', 'C', 'F', 'A', 'B'}