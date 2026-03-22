from django.db import models

# GUID -
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"image for {self.product.name}"

