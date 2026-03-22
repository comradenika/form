from django.shortcuts import render, get_object_or_404
from .models import Product

# template - html files + python code  (JINJA)
# yvela productis chveneba 
def product_list(request):
    products = Product.objects.all()
    # print(products) # queryset 
    # <QuerySet [<Product: Python-Spot<QuerySet [<Product: Python-Spotify>, <Product: NotificationService>]>
    return render(request, "products/product_list.html", {"products": products })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product })

# mvc -> mvt 
