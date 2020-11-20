from django.db import models

# Create your models here.
### test with variables before using db ###

CATEGORIES = []

PRODUCTS = [
	{'name': 'nutella', 'category': 'sucrerie'},
	{'name': 'dragibus', 'category': 'sucrerie'},
	{'name': 'ketchup', 'category': 'condiment'},
	{'name': 'chips', 'category': 'aperitif'}	
]
for product in PRODUCTS:
	if product['category'] not in CATEGORIES:
		CATEGORIES.append(product['category']) 
