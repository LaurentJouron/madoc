.. _branch :

========
Branches
========

Les branches GitHub sont des fonctionnalités essentielles pour la gestion collaborative des projets. 
Elles permettent d'organiser le développement de manière efficace en isolant les différentes fonctionnalités 
ou tâches.

Les branches offrent un environnement isolé pour travailler sur des fonctionnalités spécifiques ou des correctifs 
sans perturber le code principal (appelé souvent la branche "master" ou "main"). Cela évite les conflits entre les 
modifications en cours de développement.

Elles facilitent la collaboration en permettant à plusieurs développeurs de travailler sur des aspects différents 
du projet simultanément. Chaque développeur peut créer sa propre branche pour implémenter une nouvelle 
fonctionnalité ou résoudre un problème, puis fusionner ses changements une fois qu'ils ont été testés et approuvés.

De plus, les branches sont également utiles pour gérer les versions du logiciel. 
Par exemple, une branche de développement peut être utilisée pour intégrer de nouvelles fonctionnalités, tandis 
qu'une branche de production peut être utilisée pour déployer des versions stables et testées du logiciel.

En résumé, les branches GitHub offrent une façon structurée et sécurisée de développer des projets de manière 
collaborative, en permettant une organisation efficace du travail et en facilitant la gestion des versions du 
logiciel.


Lister les Branches
-------------------

.. code-block:: shell

    git branch

Si le projet vient juste d'être créer, il n'y aura qu'une seule branche. L’étoile indique que c’est la branche 
sur laquelle on se trouve.

.. code-block:: shell

    ""resultats""

    * main


Création d'une branche
----------------------

.. code-block:: shell

    git branch <branch name>

.. code-block:: shell

    git branch

.. code-block:: shell

    ""resultats""

    * main
    <branch name>


Changer de branches
-------------------

.. code-block:: shell

    git checkout <branch name>

.. code-block:: shell

    git branch

.. code-block:: shell

    ""resultats""

    main
    * <branch name>

Créer une branche et se positionner dessus directement

.. code-block:: shell
    
    git checkout -b <branch name>


L'Index, le Dépôt Local et le SHA
---------------------------------

L'index, également appelé stage, désigne l'ensemble des fichiers modifiés que vous souhaitez inclure dans votre prochain commit. 
Vous utilisez la commande ``git add`` pour ajouter un fichier à l'index.

Le dépôt local représente l'historique de toutes vos actions dans le projet, y compris les commits, les configurations, etc... 
L'archivage des modifications se fait principalement à l'aide de la commande ``git commit``. Vous pouvez accéder à cet historique 
en utilisant la commande ``git reflog``, qui affiche toutes vos actions passées avec leurs identifiants SHA. 
Le SHA (Secure Hash Algorithm) est un code unique qui identifie de manière spécifique chaque commit. 
Il vous permet de revenir à un commit exact à tout moment.

En résumé, l'index vous permet de préparer vos modifications pour le prochain commit, le dépôt local stocke l'historique complet de 
vos actions et le SHA est un identifiant unique pour chaque commit, permettant un contrôle précis de l'historique du projet.


Suppression d'une Branche
-------------------------

Il peut arriver que nous souhaitions ajouter nos fichiers avant de créer la branche, ce qui peut entraîner une erreur. 
Dans ce cas, nous pouvons supprimer la branche nouvellement créée en utilisant la commande :

.. code-block:: shell
    
    git branch -d NomDeLaBranche

Cela supprime la branche spécifiée, nous permettant de préparer nos fichiers avant de créer une nouvelle branche. Si des 
modifications ont déjà été apportées dans la branche que nous souhaitons supprimer, nous devrons soit faire un commit de ces 
modifications, soit les mettre de côté. Sinon, nous pouvons forcer la suppression de la branche en utilisant la commande :

.. code-block:: shell
    
    git branch -D NomDeLaBranche

Cela supprimera la branche même si des modifications y ont été apportées, mais cela peut entraîner la perte de données non 
sauvegardées. Veillez donc à utiliser cette commande avec prudence.

En suivant ces étapes, nous pouvons créer et supprimer des branches dans Git de manière efficace, en nous assurant que 
notre travail est organisé et sécurisé.


Remise et récupération des modifications
----------------------------------------

Lorsque vous modifiez votre branche main par erreur avant de créer une nouvelle branche, vous pouvez utiliser la fonction 
la remise pour mettre vos modifications de côté. Voici comment procéder :

Utilisation de la Remise (Stash)

Tout d'abord, assurez-vous que votre branche main est propre en exécutant la commande suivante :

.. code-block:: shell

    git stash

Cela mettra de côté vos modifications en cours, laissant votre branche main propre pour créer une nouvelle branche.


Création d'une Nouvelle Branche
-------------------------------

Maintenant que votre branche main est propre, vous pouvez créer une nouvelle branche avec la commande :

.. code-block:: shell

    git branch NouvelleBranche


Basculer sur la Nouvelle Branche
--------------------------------

Basculez sur la nouvelle branche que vous venez de créer en utilisant la commande :

.. code-block:: shell

    git checkout NouvelleBranche


Appliquer la Remise
-------------------

Enfin, appliquez la remise pour récupérer vos modifications sur la nouvelle branche avec la commande :


.. code-block:: shell

    git stash apply

Gérer les Remises Multiples (Optionnel)

Si vous avez plusieurs remises et que vous souhaitez appliquer une remise spécifique, vous pouvez lister les remises avec la commande :

.. code-block:: shell

    git stash list

Ensuite, appliquez la remise souhaitée en utilisant son identifiant :

.. code-block:: shell

    git stash apply stash@{Identifiant}

Vérifiez que vos modifications ont bien été appliquées en utilisant :

.. code-block:: shell

    git status

Si tout semble correct, vous pouvez maintenant effectuer un commit sur votre nouvelle branche avec vos modifications.


Annuler le dernier commit
-------------------------

Maintenant, nous allons devoir récupérer l'identifiant du commit que nous venons de réaliser. Utilisez la commande 
suivante pour afficher l'historique des commits et trouvez l'identifiant du commit que vous venez de réaliser :

.. code-block:: shell

    git log

Une fois que vous avez l'identifiant du commit (le hash), gardez-le de côté. Ensuite, assurez-vous que vous 
êtes sur votre branche main en exécutant la commande :

.. code-block:: shell

    git checkout main

Maintenant, nous allons annuler le dernier commit sur la branche master avec la commande :

.. code-block:: shell

    git reset --hard HEAD^

Après avoir annulé le dernier commit, vous pouvez créer votre nouvelle branche avec la commande :

.. code-block:: shell

    git branch nouvelle_branche

Basculez sur cette nouvelle branche avec la commande :

.. code-block:: shell

    git checkout nouvelle_branche

Enfin, appliquez les modifications du commit précédent sur votre nouvelle branche avec la commande :

.. code-block:: shell

    git cherry-pick identifiant_du_commit

Lorsque l'on travaille sur un projet avec Git, il est très important, lorsque l'on propage les modifications, 
de bien marquer dans le message descriptif les modifications que l'on a effectuées. 
Si jamais vous faites une erreur dans l'un de vos messages de commit, il est tout à fait possible de changer 
le message après coup.

.. attention::
    
    Cette commande va fonctionner pour le dernier commit réalisé !

Imaginons que vous veniez de faire un commit et que vous ayez fait une erreur dans votre message. 
L'exécution de cette commande, lorsqu'aucun élément n'est encore modifié, vous permet de modifier 
le message du commit précédent sans modifier son instantané. L'option -m permet de transmettre le nouveau message.

.. code-block:: shell

    git commit --amend -m "Votre nouveau message de commit"

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>