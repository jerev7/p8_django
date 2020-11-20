# from django.shortcuts import render
from django.http import HttpResponse
from .models import PRODUCTS, CATEGORIES


# Create your views here.
def index(request):
	message = "Salut tout le monde !\nPour voir la liste ajoute /myapp à l'url ci dessus !"
	return HttpResponse(message)

def listing(request):
	categories = ["<li>{}</li>".format(category) for category in CATEGORIES]
	message = """<ul>{}</ul>""".format("\n".join(categories))
	return HttpResponse(message)

def detail(request, category_id):
	id = int(category_id)
	category = CATEGORIES[id]
	products = []
	for product in PRODUCTS:
		if product['category'] == category:
			products.append(product['name'])
	products2 = ["<li>{}</li>".format(product) for product in products]
	message = "Les produits présents dans la categorie {} sont :\n".format(category) + """<ul>{}</ul>""".format("\n".join(products2))
	return HttpResponse(message)