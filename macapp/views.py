from itertools import product
import random
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from macapp.models import Inventory, Product, Shop

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

# About Page
def about(request):
    return render(request, 'about.html')


# Displaying on the homepage
def product_list(request):
    products = Product.objects.all()  
    return render(request, 'homepage.html', {'products': products})

def master_page(request):
    return render(request, 'hello.html')

# Displaying products list
def shop_list(request):
    shopping = Shop.objects.all()
    return render(request, 'products_list.html', {'products': shopping} )

def inventory_list(request):
    products = Product.objects.all() # Fetch all products from the database.
    return render(request, 'inventory_list.html', {'products': products})


# Categories section
def shopping_list(request):
    categories = Inventory.objects.values_list('category', flat=True).distinct()  # Get distinct categories
    products = Inventory.objects.all()  # Get all products

    # Filtering products based on category if specified
    category_filter = request.GET.get('category')
    if category_filter:
        products = products.filter(category=category_filter)

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shopping.html', context)



def shopping_page(request):
    categories = Inventory.objects.values_list('category', flat=True).distinct()  # Get unique categories
    products = Inventory.objects.all()  # Get all products

    return render(request, 'hello.html', {'categories': categories, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Inventory, id=product_id)
    
    # Exclude the current product and get random items
    more_items = list(Inventory.objects.exclude(id=product_id))
    random.shuffle(more_items)  # Shuffle to get different results each time
    more_items = more_items[:4]  # Limit to 4 items

    return render(request, 'product_detail.html', {'product': product, 'more_items': more_items})

def product_list(request):
    # Fetch products, limit to the latest 8 items
    products = Inventory.objects.all()[:8]
    return render(request, 'homepage.html', {'products': products})