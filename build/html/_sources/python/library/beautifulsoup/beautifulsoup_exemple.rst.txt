.. _beautifulsoup_exemple :

=====================
Exemple Beautifulsoup
=====================

Exploration de code Python à l'aide de BeautifulSoup et Requests pour effectuer du web scraping, 
en particulier pour découvrir les technologies utilisées par un site Web désigné.

Installation
------------

Installation de Requests

.. tab:: pipenv
    
    .. code-block:: shell

        pipenv install requests

.. tab:: pip

    .. code-block:: shell

        pip install requests


Installation de BeautifulSoup

.. tab:: pipenv
    
    .. code-block:: shell

        pipenv install beautifulsoup4

.. tab:: pip

    .. code-block:: shell

        pip install beautifulsoup4


Import des bibliothèques dans un fichier Python

.. code-block:: Python

    import requests
    from bs4 import BeautifulSoup


Définir les fonctions
---------------------

get_html_content(url) enverra une requête GET à l'URL fournie et renverra le contenu HTML de la page Web.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def get_html_content(url):
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            return response.text
        except Exception as e:
            print(f"Error occurred while fetching HTML content: {e}")
            return None


Définir une autre fonction nommée extract_meta_tags(html_content) qui extrait toutes les balises méta du contenu HTML.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def extract_meta_tags(html_content):
        try:
            # Parse the HTML content of the page
            soup = BeautifulSoup(html_content, 'html.parser')
            # Extracting meta tags for technology detection
            meta_tags = soup.find_all('meta')
            return meta_tags
        except Exception as e:
            print(f"Error occurred while extracting meta tags: {e}")
            return []


Définir une autre fonction nommée extract_script_tags(html_content) pour extraire toutes les balises de script du contenu HTML fourni.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def extract_script_tags(html_content):
        try:
            # Parse the HTML content of the page
            soup = BeautifulSoup(html_content, 'html.parser')
            # Extracting script tags for JavaScript libraries
            script_tags = soup.find_all('script')
            return script_tags
        except Exception as e:
            print(f"Error occurred while extracting script tags: {e}")
            return []


Nous définirons une fonction nommée extract_technologies_from_meta_tags(meta_tags)pour extraire les technologies mentionnées dans les balises méta fournies.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def extract_technologies_from_meta_tags(meta_tags):
        technologies = set()
        for tag in meta_tags:
            # Check for technology-related meta tags
            if 'name' in tag.attrs and 'content' in tag.attrs:
                if tag['name'].lower() in ['generator', 'framework', 'cms', 'platform']:
                    technologies.add(tag['content'])
        return technologies


Définirons une autre fonction nommée extract_technologies_from_script_tags(script_tags) pour extraire les technologies des URL de la bibliothèque JavaScript mentionnées dans les balises de script.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def extract_technologies_from_script_tags(script_tags):
        technologies = set()
        for tag in script_tags:
            # Check for JavaScript library URLs
            if 'src' in tag.attrs:
                src = tag['src']
                # Extracting library name from URL
                if '/' in src:
                    library = src.split('/')[-1].split('.')[0]
                    technologies.add(library)
        return technologies


Création d'une fonction nommée get_detected_technologies(url) qui orchestre le processus de détection des technologies utilisées dans un site Web.

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    def get_detected_technologies(url):
        html_content = get_html_content(url)
        if html_content:
            meta_tags = extract_meta_tags(html_content)
            script_tags = extract_script_tags(html_content)
            technologies_from_meta_tags = extract_technologies_from_meta_tags(meta_tags)
            technologies_from_script_tags = extract_technologies_from_script_tags(script_tags)
            detected_technologies = technologies_from_meta_tags.union(technologies_from_script_tags)
            return detected_technologies
        else:
            return None


Bloc principal
--------------

.. code-block:: Python
    :emphasize-lines: 1
    :linenos:

    if __name__ == "__main__":
        website_url = input("Enter the URL of the website: ")
        detected_technologies = get_detected_technologies(website_url)
        
        if detected_technologies:
            print("Technologies used in the website:")
            for tech in detected_technologies:
                print(tech)
        else:
            print("Failed to detect technologies.")


Exécution du code
-----------------

Après avoir consolidé tous les codes de fonction individuels dans un seul fichier Python, lors de l'exécution du script et de la fourniture d'une entrée URL de site Web, le script affichera les technologies utilisées par le site Web, comme le montre l'image ci-jointe.

.. code-block:: shell

    Enter the URL of the website: ***********
    Technologies used in the website:
    dark-mode
    fontend-custom
    sassy-social-share-public
    mpp-frontend
    jquery
    endless-river
    adsbygoogle
    WordPress 6.5.2
    custom
    wdv-about-me-widget-public
    navigation
    jquery-migrate
    slick

.. note::

    .. raw:: html

        <strong>Auteur : <a href="https://laurentjouron.github.io/" target=_blank>Laurent Jouron</a></strong>
        <strong>Envoyez moi un <a href="mailto:jouronlaurent@hotmail.com" target=_blank>e-mail</a></strong>