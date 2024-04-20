.. _binary_tree :

=============
Arbre binaire
=============

Un arbre binaire est une structure de données hiérarchique composée de nœuds, où chaque nœud a au plus deux 
enfants, généralement appelés fils gauche et fils droit. Le nœud au sommet de l'arbre est appelé la racine, 
et chaque nœud peut avoir zéro, un ou deux enfants.

Les arbres binaires sont utilisés pour stocker et organiser des données de manière efficace. Voici quelques 
utilisations courantes des arbres binaires :

- Représentation hiérarchique des données: Les arbres binaires sont souvent utilisés pour représenter des structures de données hiérarchiques telles que des arbres de fichiers dans un système de fichiers, des arbres généalogiques, des structures organisationnelles, etc.
- Recherche et tri efficaces: Les arbres binaires de recherche (ABR) sont des structures de données qui permettent de stocker des données de manière ordonnée et de réaliser des opérations de recherche et de tri efficaces. Les ABR garantissent que les données sont organisées de manière à ce que les opérations de recherche puissent être effectuées en un temps logarithmique par rapport à la taille de l'arbre.
- Implémentation de structures de données avancées: Les arbres binaires sont utilisés comme composants de base dans de nombreuses structures de données avancées telles que les tas binaires, les arbres AVL, les arbres rouge-noir, etc. Ces structures de données offrent des performances optimales pour des opérations spécifiques telles que l'insertion, la suppression et la recherche.
- Analyse et traitement de données: Les arbres binaires sont utilisés dans l'analyse de données et le traitement de données pour représenter des hiérarchies de données complexes et pour effectuer des opérations telles que l'agrégation, la recherche de chemins, etc. 

En résumé, les arbres binaires sont des structures de données polyvalentes utilisées dans de nombreux domaines de l'informatique pour stocker, organiser et manipuler des données de manière efficace et structurée. Ils offrent une grande flexibilité et sont largement utilisés dans le développement de logiciels pour diverses applications.

Fonction
--------

.. code-block:: Python

    class TreeNode:
    """Class representing a node in a binary tree."""
    def __init__(self, data):
        """Initializes a node with data and left and right pointers.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None


    def depth_of_tree(tree):
        """Recursive function to find the depth of a binary tree.

        Args:
            tree (TreeNode): The root node of the tree.

        Returns:
            int: The depth of the tree.
        """
        if tree is None:
            return 0
        else:
            depth_left_tree = depth_of_tree(tree.left)
            depth_right_tree = depth_of_tree(tree.right)
            if depth_left_tree > depth_right_tree:
                return 1 + depth_left_tree
            else:
                return 1 + depth_right_tree


    def is_full_binary_tree(tree):
        """Function to check if a binary tree is full.

        Args:
            tree (TreeNode): The root node of the tree.

        Returns:
            bool: True if the tree is full, False otherwise.
        """
        if tree is None:
            return True
        if (tree.left is None) and (tree.right is None):
            return True
        if (tree.left is not None) and (tree.right is not None):
            return is_full_binary_tree(tree.left) and is_full_binary_tree(tree.right)
        else:
            return False


    def main():
        """Main function for testing.

        Creates a binary tree, then checks if it's full and calculates its depth.
        """
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left.left = TreeNode(4)
        tree.left.right = TreeNode(5)
        tree.left.right.left = TreeNode(6)
        tree.right.left = TreeNode(7)
        tree.right.left.left = TreeNode(8)
        tree.right.left.left.right = TreeNode(9)

        print(is_full_binary_tree(tree))
        print(depth_of_tree(tree))

.. tab:: Utilisation
    
    .. code-block:: Python

        if __name__ == '__main__':
            main()

.. tab:: Resultats

    .. code-block:: Python

        False
        5

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
