from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=25, unique=True)
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


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=20)


class RatingReview(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(default=0)
    reviews = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)
