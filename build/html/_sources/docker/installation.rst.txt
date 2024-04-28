.. _installation :

============
Installation
============

Vérification des prérequis : Avant d'installer Docker, il faut s'assure que le système répond aux exigences 
minimales. Docker est compatible avec de nombreuses distributions Linux, Windows 10 64-bit: Pro, 
Enterprise, or Education (build 16299 ou supérieur), et macOS 10.13 ou version ultérieure.

Installation sur Linux :

Pour les distributions basées sur Debian (comme Ubuntu), utilise les commandes suivantes dans un terminal :


.. tab:: Unix

    .. code-block:: shell

        sudo apt-get update

    .. code-block:: shell

        sudo apt-get install docker-ce docker-ce-cli containerd.io



Pour les distributions basées sur `Red Hat <https://www.redhat.com/fr>`_ (comme `CentOS <https://www.centos.org/>`_), consulte la documentation officielle de Docker pour obtenir les instructions spécifiques.
Installation sur Windows :

Télécharge et exécute l'installateur Docker Desktop pour Windows à partir du site officiel de Docker.
Suivre les instructions à l'écran pour installer Docker Desktop.
Installation sur macOS :

Télécharge et installe Docker Desktop pour Mac à partir du site officiel de Docker.
Ouvre le fichier téléchargé et glisse l'icône Docker dans le dossier Applications.
Vérification de l'installation : Une fois l'installation terminée, vérifie que Docker est correctement installé en exécutant la commande suivante dans un terminal ou une invite de commande :

.. code-block:: shell

    docker --version

Exécution du conteneur de test : Pour vérifier que Docker fonctionne correctement, tu peux exécuter un conteneur de test en utilisant la commande suivante :

.. code-block:: shell

    docker run hello-world

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>