from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Product Name')
    image = models.ImageField(verbose_name='Image', blank=True, upload_to='product_images/')
    price = models.IntegerField(verbose_name='Item Price')

    def __str__(self):
        return f"Price of {self.name} is Kshs: {self.price}/="

class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name='Product Name')
    image = models.ImageField(verbose_name='Image', blank=True, upload_to='product_images/')
    price = models.IntegerField(verbose_name='Item Price')
    description = models.TextField(max_length=250, verbose_name='Product Description', blank=True)

    def __str__(self):
        return f"This product is {self.name}"

class Inventory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Product Name", unique=True)  # Unique name for each product
    description = models.TextField(blank=True, null=True, verbose_name="Description") # Optional description
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price") # Price with decimal places
    quantity_in_stock = models.PositiveIntegerField(default=0, verbose_name="Quantity in Stock")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Product Image") # Optional image
    category = models.CharField(max_length=25, verbose_name="Product Category")
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically adds creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updates timestamp on modification

    def __str__(self):
        return self.name
