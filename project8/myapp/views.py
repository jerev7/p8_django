# from django.shortcuts import render
from django.http import HttpResponse
from .models import PRODUCTS, CATEGORIES
from .models import Category, Products
from django.template import loader


# Create your views here.
def index(request):
	categories = Category.objects.all()
	template = loader.get_template('myapp/index.html')
	context = {'categories': categories}
	return HttpResponse(template.render(context, request=request))

def listing(request):
	categories = ["<li>{}</li>".format(category) for category in CATEGORIES]
	message = """<ul>{}</ul>""".format("\n".join(categories))
	return HttpResponse(message)

def detail(request, category_id):
	id = int(category_id)
	category = Category.objects.get(pk=id)
	products = category.product.all()
	template = loader.get_template('myapp/detail.html')
	context = {'products': products}
	return HttpResponse(template.render(context, request=request))