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


class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name


class Products(models.Model):
	name = models.CharField(max_length=200)
	palm_oil = models.BooleanField(default=False)
	gluten = models.BooleanField(default=False)
	stores = models.CharField(max_length=200)
	url = models.CharField(max_length=200)
	categories = models.ManyToManyField(Category, related_name='product', blank=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name
