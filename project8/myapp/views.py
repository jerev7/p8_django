from django.shortcuts import render
from django.http import HttpResponse
from .models import PRODUCTS, CATEGORIES
from .models import Category, Products
from django.template import loader


# Create your views here.
def index(request):
	categories = Category.objects.all()
	context = {'categories': categories}
	return render(request, 'myapp/index.html', context)


def listing(request):
	categories = ["<li>{}</li>".format(category) for category in CATEGORIES]
	message = """<ul>{}</ul>""".format("\n".join(categories))
	return HttpResponse(message)

def detail(request, category_id):
	id = int(category_id)
	category = Category.objects.get(pk=id)
	products = category.product.all()
	context = {'products': products}
	return render(request, 'myapp/detail.html', context)
