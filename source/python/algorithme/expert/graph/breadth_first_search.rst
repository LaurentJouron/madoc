.. _breadth_first_search :

====================
Breadth-First Search
====================

    La recherche en largeur (Breadth-First Search ou BFS en anglais) est un algorithme utilisé pour parcourir ou rechercher des structures de données arborescentes ou de graphe. Il démarre à partir d'un nœud racine spécifié et explore tous les nœuds voisins à la profondeur actuelle avant de passer aux nœuds de la prochaine profondeur.

    Commencez avec une structure de file d'attente pour suivre les nœuds à visiter. Initialement, mettez le nœud de départ dans la file d'attente.
    Créez un ensemble pour garder une trace des nœuds explorés.
    Défilez un nœud de la file d'attente et marquez-le comme exploré.
    Mettez dans la file d'attente tous les nœuds voisins non explorés du nœud défilé.
    Répétez les étapes 3-4 jusqu'à ce que la file d'attente soit vide.

    BFS explore tous les nœuds voisins à la profondeur actuelle avant de passer aux nœuds de la prochaine profondeur. Cela garantit qu'il parcourt le graphe de manière en largeur.
    BFS peut être utilisé pour trouver le plus court chemin dans un graphe non pondéré car il explore toujours les nœuds dans l'ordre croissant de leur distance par rapport au nœud de départ.

    Trouver le plus court chemin entre deux nœuds dans un graphe non pondéré.
    Détecter les cycles dans un graphe.
    Résoudre des casse-têtes comme le plus court chemin dans un labyrinthe.

    Complexité temporelle : O(V + E), où V est le nombre de sommets (nœuds) et E est le nombre d'arêtes dans le graphe.
    Complexité spatiale : O(V), où V est le nombre de sommets. Cela est dû au fait que BFS doit garder une trace de tous les nœuds visités en mémoire.

    mathematica

.. code-block:: Python

         A
       /   \
      B     C
     / \   / \
    D   E F   G


En partant du nœud A, BFS visiterait les nœuds dans l'ordre : A, B, C, D, E, F, G.

La recherche en largeur est un algorithme fondamental pour parcourir et rechercher des graphes. Sa simplicité et son efficacité en font un choix populaire pour divers problèmes liés aux graphes.

Fonction
--------

.. code-block:: Python
    :emphasize-lines: 1,3
    :linenos:
    
    import collections

    def bfs(graph, start):
        """
        Perform Breadth-First Search (BFS) on a graph starting from a given node.

        Args:
            graph (dict): The graph represented as a dictionary where keys are nodes and values are lists of neighboring nodes.
            start: The starting node for BFS traversal.

        Returns:
            set: A set containing all nodes explored during BFS traversal.
        """
        explored, node_queue = set(), [start]
        explored.add(start)
        while node_queue:
            current_node = node_queue.pop(0)
            for neighbor in graph[current_node]:
                if neighbor not in explored:
                    explored.add(neighbor)
                    node_queue.append(neighbor)
        return explored


    graph = {'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']}

.. tab:: Utilisation
    
    .. code-block:: Python
    
        print(bfs(graph, 'A'))

.. tab:: Resultats

    .. code-block:: shell

        {'D', 'E', 'C', 'F', 'A', 'B'}

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>