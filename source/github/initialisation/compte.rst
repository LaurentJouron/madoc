.. _compte :

====================
Création d'un compte
====================

Avant de commencer il faut créer un compte `github <https://github.com/>`_.

Installation de Git sur votre ordinateur
----------------------------------------

Rendez-vous sur la page de téléchargement de `Git <https://git-scm.com/downloads>`_ et téléchargez les fichiers d'installation compatibles 
avec votre système d'exploitation. L'installation est similaire sur tous les systèmes d'exploitation, mais assurez-vous de télécharger 
la version compatible avec votre OS. Une fois téléchargé, exécutez le fichier d'installation et suivez les instructions à l'écran. 
Assurez-vous de cocher l'option launch Git Bash à la dernière étape de l'installation.


Initialisation
--------------

La première étape consiste à configurer votre compte Git. Utilisez les commandes suivantes en remplaçant les valeurs entre guillemets par 
vos propres informations :

.. code-block:: shell

    git config --global user.username "VotreNomUtilisateur"

.. code-block:: shell

    git config --global user.email "votre@email.com"


Si vous souhaitez configurer ces paramètres uniquement pour un projet spécifique, exécutez les mêmes commandes sans l'option --global.

Pour vérifier que les paramètres ont été correctement pris en compte et voir d'autres paramètres configurés, utilisez la commande :

.. code-block:: shell
    
    git config --list

.. code-block:: shell

    """Resultat"""

    diff.astextplain.textconv=astextplain
    filter.lfs.clean=git-lfs clean -- %f
    filter.lfs.smudge=git-lfs smudge -- %f
    filter.lfs.process=git-lfs filter-process
    filter.lfs.required=true
    http.sslbackend=schannel
    core.autocrlf=true
    core.fscache=true
    core.symlinks=false
    core.editor="C:\\Program Files (x86)\\Notepad++\\notepad++.exe" -multiInst -notabbar -nosession -noPlugin
    pull.rebase=false
    credential.helper=manager-core
    credential.https://dev.azure.com.usehttppath=true
    init.defaultbranch=master
    filter.lfs.clean=git-lfs clean -- %f
    filter.lfs.smudge=git-lfs smudge -- %f
    filter.lfs.process=git-lfs filter-process
    filter.lfs.required=true


Configuration avancée
---------------------

Il est recommandé d'activer les couleurs pour améliorer la lisibilité des informations affichées par Git. 
Exécutez les commandes suivantes dans Git Bash :

.. code-block:: shell

    git config --global color.diff auto


.. code-block:: shell

    git config --global color.status auto

.. code-block:: shell

    git config --global color.branch auto


Par défaut, Git utilise Vim comme éditeur et Vimdiff comme outil de merge. Si vous préférez utiliser un autre 
éditeur ou outil de merge, vous pouvez le configurer en utilisant les commandes suivantes :

.. code-block:: shell

    git config --global core.editor NomDeVotreEditeur

.. code-block:: shell

    git config --global merge.tool NomDeVotreOutilDeMerge

Il est également possible de modifier le nom de la branche principale de votre dépôt Git de "master" à "main" en utilisant la commande suivante :

.. code-block:: shell

    git config --global init.defaultBranch main

Cette modification n'est pas obligatoire, mais elle est recommandée pour des raisons de standardisation et de compatibilité avec d'autres dépôts.