.. _compte :

====================
Creation d'un compte
====================

Avant de commencer il faut créer un compte `github <https://github.com/>`_.

Installer git sur son ordinateur
--------------------------------

Rendez-vous sur la page de `git <https://git-scm.com/downloads>`_. Ensuite il faut télécharger les fichiers d'installation. 
L'installation est la même sur tous les OS, mais il faut télécharger la version compatible avec le système.
Lancer l'executable et cliquer sur suivant, sauf à la dernière fenêtre où il faut cocher **launch Git Bash**.

Initialisation
--------------

La première chose à faire est d'initialiser son compte. Pour ça il faut saisir les lignes de commandes. Cet exemple montre l'initialisation 
de **mon** compte.

.. code-block:: shell

    git config --global user.username "Laurent Jouron"

.. code-block:: shell

    git config --global user.email "jouronlaurent@hotmail.com"

Pour un projet spécifique, changer le nom d’utilisateur,Il faut repasser cette ligne mais sans le --global.

Pour vérifier que les paramètres aient bien été pris en compte, et vérifier les autres paramètres, 
il suffit de passer la commande 

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

Je recommande d’activer les couleurs pour améliorer la lisibilité des branches. Passez ces trois lignes dans Git Bash:

.. code-block:: shell

    git config --global color.diff auto


.. code-block:: shell

    git config --global color.status auto

.. code-block:: shell

    git config --global color.branch auto

Par défaut, Git utilise Vim comme éditeur et Vimdiff comme outil de merge. Pour les modifier utilise:

.. code-block:: shell

    git config --global core.editor notepad++

.. code-block:: shell

    git config --global merge.tool vimdiff

Il y a un changement qui n'a aucun impact mais qui fait beaucoup parler, c'est le nom de la branche principal. Pour passer de master à main 
il faut utiliser cette commande.
Ce n’est clairement pas obligatoire. Votre branche principale peut avoir le nom que l'on souhaite. Cela dépend surtout des convictions de chacun.
Je vous recommande de la faire car cela permet d’avoir un nom qui correspond à la norme et cela ça permet d'échanger simplement 
avec d’autres développeurs.

.. code-block:: shell

    git config --global init.defaultBranch main
