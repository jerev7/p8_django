from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name


class Products(models.Model):
	name = models.CharField(max_length=200)
	nutriscore = models.IntegerField()
	image_url = models.URLField(max_length=200)
	url_offacts = models.URLField(max_length=200)
	energy_value = models.CharField(max_length=200)
	energy_unit = models.CharField(max_length=200)
	sugars_100g = models.CharField(max_length=200)
	fat_100g = models.CharField(max_length=200)
	saturated_fat_100g = models.CharField(max_length=200)
	proteins = models.CharField(max_length=200)
	nutriscore_letter_url = models.URLField(max_length=200)
	nutriscore_complete_url = models.URLField(max_length=200)
	categories = models.ManyToManyField(Category, related_name='product', blank=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name
