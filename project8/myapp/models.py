from django.db import models

# Create your models here.
### test with variables before using db ###




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
	categories = models.ManyToManyField(Category, related_name='product', blank=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name
