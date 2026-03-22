from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)
    categories = Product.CATEGORY_CHOICES
    return render(request, "products/product_list.html", {
        "products": products,
        "categories": categories,
        "selected_category": category,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"product": product})

