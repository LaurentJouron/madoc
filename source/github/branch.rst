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

.. code-block:: console

    git branch


Si le projet vient juste d'être créer, il n'y aura qu'une seule branche. L’étoile indique que c’est la branche 
sur laquelle on se trouve.

.. code-block:: console

    ""resultats""
    * main


Création d'une branche
----------------------

.. code-block:: console

    git branch <branch name>

.. code-block:: console

    git branch

.. code-block:: console

    ""resultats""
    * main
    <branch name>


Changer de branches
-------------------

.. code-block:: console

    git checkout <branch name>

.. code-block:: console

    git branch

.. code-block:: console

    ""resultats""
    main
    * <branch name>

Créer une branche et se positionner dessus directement

.. code-block:: console
    
    git checkout -b <branch name>