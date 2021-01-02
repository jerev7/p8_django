from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Category, Products
from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



# Create your views here.
def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'myapp/index.html', context)


# def listing(request):
#   categories = ["<li>{}</li>".format(category) for category in CATEGORIES]
#   message = """<ul>{}</ul>""".format("\n".join(categories))
#   return HttpResponse(message)

def results(request, product_id):
    id = int(product_id)
    product_selected = get_object_or_404(Products, pk=id)
    category = get_object_or_404(Category, product__id=product_selected.id)
    # category = get_object_or_404(Category, pk=id)
    product_list = category.product.filter(nutriscore__lt = product_selected.nutriscore)
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'paginate': True,
        'product_selected': product_selected
    }
    return render(request, 'myapp/results.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        product_list = Products.objects.all()
    else:
        product_list = Products.objects.filter(name__icontains=query)
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    # if len(categories) == 0:
    #     categories = Category.objects.filter(product__name__icontains=query)

    if len(products) == 0:
        raise Http404
    context ={
        'paginate': True,
        'products': products,
        'query': query
    }
    return render(request, 'myapp/search.html', context)
