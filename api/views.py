from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from django.http import JsonResponse


# Seller


class SellerList(generics.ListCreateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer


# Product


class ProductCategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer


class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


# Buyer


class BuyerList(generics.ListCreateAPIView):
    queryset = models.Buyer.objects.all()
    serializer_class = serializers.BuyerSerializer


# Rating


class RatingReviewList(generics.ListCreateAPIView):
    queryset = models.RatingReview.objects.all()
    serializer_class = serializers.RatingReviewSerializer

    def get_queryset(self):
        if "product_id" in self.request.GET:
            product_id = self.kwargs["product_id"]
            product = models.Product.objects.get(pk=product_id)
            return models.RatingReview.objects.filter(product=product)


def buyerRatingStatus(request, buyer_id, product_id):
    buyer = models.Buyer.objects.filter(pk=buyer_id).first()
    product = models.Product.objects.filter(pk=product_id).first()
    ratingStatus = models.RatingReview.objects.filter(buyer=buyer, product=product)
    if ratingStatus:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})
