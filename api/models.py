from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to="seller_profile_imgs/", null=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    description = models.TextField()
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    img = models.ImageField(upload_to="product_imgs/", null=True)
