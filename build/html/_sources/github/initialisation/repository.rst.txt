.. _repository :

==========
Repository
==========

Création d'un repository
------------------------

Il faut se déplacer dans le dossier où l'on veux placer le projet.

.. code-block:: console

    cd C:\Users\l.jouron\VisualStudioCode

Créer un dossier au nom du projet.

.. code-block:: console

    mkdir projet

Se placer dans le dossier.

.. code-block:: console

    cd projet

Initialiser le projet avec ses paramètrages.

.. code-block:: console

    git init

Le dossier n’a rien de nouveau, mais c’est normal. Pourtant bien initialisé par Git. Il y a un dossier caché .git qui a été créé. 
Pour le voir aller dans Affichage, puis éléments masqués.


Accéder à un depot distant
--------------------------

Comment accéder à un dépôt distant et le cloner en local. Il faut récupérer l’URL du dépôt sur GitHub.

.. code-block:: console

    git remote add LOCAL https://github.com/LaurentJouron/madoc


Cloner à un depot distant
-------------------------

.. code-block:: console

    git clone https://github.com/LaurentJouron/madoc


Faire un commit
---------------

Avant de faire un commit il faut ajouter les fichiers nécéssaires aux modifications.

.. code-block:: console

    git add requirements.txt

Pour ajouter tous les fichiers en une seule commande:

.. code-block:: console

    git add .

Faire le commit:

.. code-block:: console

    git commit -m “First commit”

.. code-block:: console

    git push -u origin main