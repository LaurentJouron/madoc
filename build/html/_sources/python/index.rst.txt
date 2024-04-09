======
Python
======

.. important::

    .. image:: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
        :alt: Python Badge
        :target: https://docs.python.org/3/

    Tout en étant le plus proche de la documentation officielle, ces notes sont rédigées pour des projets personnels. 
    En fonction des besoins, il faut se rendre sur la documentation officielle et adapter les paramétrages 
    `Python <https://docs.python.org/3/>`_.

6. Once you fixed the issue, run the tests, and the patchcheck:

   .. tab:: Unix

      .. code-block:: shell

         make patchcheck

   .. tab:: macOS

      .. code-block:: shell

         make patchcheck

   .. tab:: Windows

      .. code-block:: dosbatch

         .\python.bat Tools\patchcheck\patchcheck.py

.. toctree::
   :maxdepth: 3

   pep8/index
   library/index
   virtual_environment/index
   algorithme/index