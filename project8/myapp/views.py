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

def detail(request, category_id):
    id = int(category_id)
    category = get_object_or_404(Category, pk=id)
    product_list = category.product.all()
    paginator = Paginator(product_list, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'paginate': True}
    return render(request, 'myapp/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
        categories = Category.objects.all()
    else:
        categories = Category.objects.filter(name__icontains=query)

    if not categories.exists():
        categories = Category.objects.filter(product__name__icontains=query)

    if len(categories) == 0:
        raise Http404
    title = "La recherche %s a pour résultat les categories suivantes :"%query
    context ={
        'categories': categories,
        'title': title,
        'query': query
    }
    return render(request, 'myapp/search.html', context)
