from django.shortcuts import render, get_object_or_404
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
	category = get_object_or_404(Category, pk=id)
	products = category.product.all()
	context = {'products': products}
	return render(request, 'myapp/detail.html', context)

def search(request):
	query = request.GET.get('query')
	if not query:
		categories = Category.objects.all()
	else:
		categories = Category.objects.filter(name__icontains=query)
	if not categories.exists():
		categories = Category.objects.filter(product__name__icontains=query)
	title = "La recherche %s a pour résultat les categories suivantes :"%query
	context ={
		'categories': categories,
		'title': title
	}
	return render(request, 'myapp/search.html', context)
