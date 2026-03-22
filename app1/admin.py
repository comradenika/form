from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'created_at')
    list_filter = ('in_stock', 'category')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]


admin.site.register(ProductImage)

