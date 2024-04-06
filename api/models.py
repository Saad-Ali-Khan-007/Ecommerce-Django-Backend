from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    img = models.ImageField(upload_to="seller_profile_imgs/", null=True)
