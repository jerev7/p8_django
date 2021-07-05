# Projet 8 - Django :

**_Description :_**

The goal of this project is to provide a website (available at https://p8django.herokuapp.com/ ) where the user can search for food products, then we offer him to choose between all the products that are almost the same as the one he wants but that are healthier.

The user can create an account with which he can save the products he chose from his previous searches.

We built the website using Django, and we got all food data from Openfoodfacts API.

For now we have data only about products in the same category as Nutella to show that it is working but we can add easily all categories we need. 

**_How to get data from Openfoodfacts :_**

To fill your database with Openfoodfacts data, first you need to set up your PostgreSQL database.

To do so you need to :
1) Create a database.
2) Update settings.py file with database information as follows :
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'project8',
        'USER': 'jeremiev',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '5432'
    }
}
"""

- clonage repo

- 