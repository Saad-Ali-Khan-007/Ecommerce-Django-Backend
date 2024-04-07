from rest_framework import serializers
from . import models


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
