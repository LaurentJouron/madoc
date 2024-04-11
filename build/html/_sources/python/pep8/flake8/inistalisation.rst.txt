.. _inistalisation :

==============
Initialisation
==============

Pour installer Flake8, ouvrir un shell interactif et exécuter:

   .. tab:: pipenv

        Avec pipenv

      .. code-block:: shell

        pipenv install flake8

   .. tab:: pip

        Avec pip

      .. code-block:: shell

        pip install flake8

   .. tab:: par defaut

        Pour installer Flake8 sur Python par défaut, utiliser.

      .. code-block:: shell

        python -m pip install flake8

.. note::

    Il est très important d’installer Flake8 sur la version correcte de Python pour les besoins. Pour que Flake8 analyse correctement les nouvelles 
    fonctionnalités de langage dans Python 3.5 (par exemple), il faut l’installer sur 3.5 pour Flake8 pour comprendre ces fonctionnalités. 
    Flake8 est lié à la version de Python sur laquelle il fonctionne.


.flake8
-------

⚙️ Création et configuration du fichier ``.flake8``. Cet exemple de configuration a été réalisée pour un projet Django. Il faut adapter pour chaque projet.

.. code-block:: Python

    [flake8]
    # it's not a bug that we aren't using all of hacking
    extend-ignore =
    # H101: Use TODO(NAME)
    H101,
    # H202: assertRaises Exception too broad
    H202,
    # H233: Python 3.x incompatible use of print operator
    H233,
    # H301: one import per line
    H301,
    # H306: imports not in alphabetical order (time, os)
    H306,
    # H401: docstring should not start with a space
    H401,
    # H403: multi line docstrings should end on a new line
    H403,
    # H404: multi line docstring should start without a leading new line
    H404,
    # H405: multi line docstring summary not separated with an empty line
    H405,
    # H501: Do not use self.__dict__ for string formatting
    H501

    max-line-length = 99

    # In .flake8 or setup.cfg, use the exclude option to specify which directories
    # or files you want to exclude from the scan.
    exclude =
    venv,
    .venv,
    .git,
    .gitignore,
    setup.py
    **/migrations/*,
    __pycache__,

    # filename option to exclude specific files rather than entire directories.
    filename =
    Lib\site-packages\urllib3\util\timeout.py,
    Lib\site-packages\urllib3\util\url.py,
    Lib\site-packages\whitenoise\base.py,
    Lib\site-packages\whitenoise\middleware.py,
    Scripts\activate_this.py

Utilisation de flake8
---------------------

Pour commencer à utiliser Flake8, ouvrez un shell interactif et exécutez

.. code-block:: shell

    flake8

Créer un rapport flake8
-----------------------

Flake8-HTML est une extension de Flake8 qui génère des rapports HTML détaillés basés sur les résultats de l’analyse de code effectuée par Flake8.


Extension Flake8
----------------

Flake8-HTML étend la fonctionnalité de Flake8 en ajoutant la possibilité de générer des rapports au format HTML à partir des résultats de 
l’analyse de code.


Rapports détaillés
------------------

Avec Flake8-HTML, on peut générer des rapports HTML détaillés qui présentent les résultats de l’analyse de code clairement et visuellement. 
Ces rapports fournissent des informations détaillées sur les violations de style, les erreurs détectées et d’autres problèmes identifiés par Flake8.


Visualisation conviviale
------------------------

Les rapports HTML générés par Flake8-HTML sont conçus pour être faciles à interpréter. Ils utilisent une mise en page structurée et des 
éléments visuels pour présenter l’information de manière compréhensible.


Personnalisable
---------------

Flake8-HTML offre également une certaine personnalisation dans les rapports. On peut configurer les options de génération pour inclure ou exclure 
certaines informations, choisir le style visuel des rapports, etc...


Intégration dans les flux de travail
------------------------------------

Flake8-HTML peut être intégré dans un workflow Python pour fournir des rapports de qualité sur la qualité du code. 
Ces rapports peuvent être utilisés pour identifier et résoudre les problèmes, améliorant la maintenabilité et la lisibilité du code.


En résumé, Flake8-HTML est une extension pratique de Flake8 qui ajoute la possibilité de générer des rapports HTML détaillés à partir 
des résultats d’analyse de code, offrant une visualisation claire et concise des problèmes de qualité de code détectés. 
L’utilisation de Flake8-HTML peut aider à maintenir un code propre, cohérent et de haute qualité dans vos projets Python.

   .. tab:: pipenv

      .. code-block:: shell

        pipenv install flake8-html

   .. tab:: pip

      .. code-block:: shell

        pip install flake8-html


.. code-block:: shell

    flake8 --format=html --htmldir=flake-report


Workflows
---------

.. code-block:: Python

    version: 2.1

    orbs:
    python: circleci/python@2.1.1

    jobs:
    run_test:
    docker:
        - image: cimg/python:3.12.0
    steps:
        - checkout
        - python/install-packages:
            pkg-manager: pipenv
        - run:
            name: Run tests
            command:
                mkdir test-results && pipenv run pytest

    flake8_test:
    docker:
        - image: cimg/python:3.12.0
    steps:
        - checkout
        - run:
            name: Install Flake8
            command: pip install flake8==3.7.0
        - run:
            name: check linting with Flake8
            command: flake8
        - store_test_results:
            path: test-results
        - store_artifacts:
            path: test-results
            destination: tr1
        - persist_to_workspace:
            root: ~/project
            paths:
                - .

    workflows:
    main:
    jobs:
        - flake8_test
        - build-docker-image:
            requires:
                - flake8_test

