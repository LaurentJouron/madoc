.. _repository :

==========
Repository
==========

Guide de démarrage rapide avec Git et VSCode
--------------------------------------------

**Se placer dans le dossier où l'on veut placer le projet**

Utilisez la commande suivante pour naviguer vers le dossier où vous souhaitez créer votre projet :

.. code-block:: shell

    cd C:\Users\Laurent\VSCode


**Créer un dossier au nom du projet**

Créez un nouveau dossier pour votre projet en utilisant la commande suivante :

.. code-block:: shell

    mkdir projet


**Se placer dans le dossier du projet**

Accédez au dossier que vous venez de créer en utilisant la commande suivante :

.. code-block:: shell

    cd projet


**Initialiser le projet avec Git**

Initialisez un nouveau dépôt Git dans votre projet en utilisant la commande suivante :

.. code-block:: shell

    git init


Le dossier n’a rien de nouveau, mais c’est normal. Pourtant bien initialisé par Git. Il y a un dossier caché .git qui a été créé. 
Pour le voir aller dans Affichage, puis éléments masqués. Le dossier .git est essentiel pour le suivi des modifications de votre 
projet à l'aide de Git. Il contient toutes les informations sur l'historique des versions, les branches, les configurations et d'autres 
métadonnées importantes. Bien que ce dossier soit caché par défaut, il joue un rôle crucial dans la gestion de votre projet avec Git.


Accéder à un depot distant
--------------------------

Pour accéder à un dépôt distant et le lier à votre dépôt local, vous devez d'abord récupérer l'URL du dépôt sur GitHub. Utilisez 
la commande suivante pour ajouter le dépôt distant à votre configuration locale :

.. code-block:: shell

    git remote add NomLocal https://github.com/NomUtilisateur/NomDépôt


Clonage d'un depot distant
--------------------------

Pour cloner un dépôt distant et créer une copie locale de celui-ci, utilisez la commande suivante en spécifiant l'URL du dépôt distant :


.. code-block:: shell

    git clone https://github.com/LaurentJouron/madoc


Faire un commit
---------------

Avant de faire un commit, assurez-vous d'avoir ajouté tous les fichiers nécessaires à vos modifications. Utilisez la commande suivante 
pour ajouter des fichiers spécifiques à votre staging area :

.. code-block:: shell

    git add nomDuFichier

Pour ajouter tous les fichiers modifiés à la staging area en une seule commande, utilisez :

.. code-block:: shell

    git add .

Ensuite, faites votre commit avec un message descriptif :

.. code-block:: shell

    git commit -m "Votre message de commit ici"

Enfin, poussez vos modifications vers le dépôt distant en spécifiant la branche à laquelle vous souhaitez pousser :

.. code-block:: shell

    git push -u origin NomBranche