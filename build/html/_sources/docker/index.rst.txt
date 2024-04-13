======
Docker
======

.. important::

    .. image:: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
        :alt: Docker Badge
        :target: https://www.sqlite.org/index.html

    Tout en étant le plus proche de la documentation officielle, ces notes sont rédigées pour des projets personnels. 
    En fonction des besoins, il faut se rendre sur la documentation officielle et adapter les paramétrages 
    `Docker <https://docs.docker.com/>`_.

Docker est une plateforme open-source qui permet de développer, de déployer et de gérer des applications 
dans des conteneurs. Un conteneur Docker est une unité logicielle légère et portable qui contient tout 
ce dont une application a besoin pour s'exécuter, y compris le code, les bibliothèques, les dépendances 
et les fichiers système.

L'une des principales caractéristiques de Docker est la possibilité de créer des environnements isolés, 
appelés conteneurs, qui sont exécutés sur un même système hôte. Cela permet aux développeurs d'emballer 
une application avec toutes ses dépendances dans un conteneur, garantissant ainsi une portabilité 
et une cohérence entre les environnements de développement, de test et de production.

En résumé, Docker simplifie le processus de développement, de déploiement et de gestion des applications 
en fournissant une méthode standardisée pour créer et exécuter des conteneurs logiciels.


.. toctree::
   :maxdepth: 3

   docker_compose/index
   dockerfile/index
   dockerhub/index
   installation