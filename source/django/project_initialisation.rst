.. _project_initialisation :

==============
Initialisation
==============

.. code-block:: shell

    mkdir <nom projet>

.. code-block:: shell

    cd <nom projet>

.. code-block:: shell

    mkdir .venv

.. tab:: pipenv

    .. code-block:: shell

        pipenv install

.. tab:: pip

    .. code-block:: shell

        pip install

Activer l'environnement

.. tab:: pipenv

    .. code-block:: shell

        pipenv shell

.. tab:: pip

    .. code-block:: shell

        source env\Scripts\activate

.. tab:: pip Mac et Unix

    .. code-block:: shell

        source env/bin/activate

installation de Django

.. tab:: pipenv
    
    .. code-block:: shell

        pipenv install django

.. tab:: pip

    .. code-block:: shell

        pip install django

.. code-block:: shell

    django-admin startptoject config .

.. code-block:: shell

    python manage.py runserver

.. raw:: html

   <a href="http://localhost:8000" class="button" target=_blank>
       <img src="../_static/_buttons/button_open_website.png" alt="Bouton" width="200" height="100" />
   </a>

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>