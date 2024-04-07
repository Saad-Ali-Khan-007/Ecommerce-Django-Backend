from rest_framework import serializers
from . import models


# Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = "__all__"


# Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"


# Buyer


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Buyer
        fields = "__all__"


# Rating


class RatingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RatingReview
        fields = "__all__"
