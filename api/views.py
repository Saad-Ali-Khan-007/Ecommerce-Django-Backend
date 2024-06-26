from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Seller


class SellerList(generics.ListCreateAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerSerializer


@csrf_exempt
def seller_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        seller_data = models.Seller.objects.get(email=email, password=password)
    except models.Seller.DoesNotExist:
        seller_data = None
    if seller_data:
        return JsonResponse({"bool": True, "seller_id": seller_data.id})
    else:
        return JsonResponse({"bool": False})


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


@csrf_exempt
def buyer_login(request):
    email = request.POST["email"]
    password = request.POST["password"]
    try:
        buyer_data = models.Buyer.objects.get(email=email, password=password)
    except models.Buyer.DoesNotExist:
        buyer_data = None
    if buyer_data:
        return JsonResponse({"bool": True, "seller_id": buyer_data.id})
    else:
        return JsonResponse({"bool": False})


# Rating


class RatingReviewList(generics.ListCreateAPIView):
    queryset = models.RatingReview.objects.all()
    serializer_class = serializers.RatingReviewSerializer

    def get_queryset(self):

        if "product_id" in self.kwargs:
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


# Wishlist


class Wishlist(generics.ListCreateAPIView):
    queryset = models.Wishlist.objects.all()
    serializer_class = serializers.WishlistSerializer

    def get_queryset(self):
        if "buyer_id" in self.kwargs:
            buyer_id = self.kwargs["buyer_id"]
            buyer = models.Buyer.objects.get(pk=buyer_id)
            return models.Wishlist.objects.filter(buyer=buyer)


def wishlist_status(request, buyer_id, product_id):
    buyer = models.Buyer.objects.filter(id=buyer_id).first()
    product = models.Product.objects.filter(id=product_id).first()
    wishlist_status = models.Wishlist.objects.filter(
        buyer=buyer, product=product
    ).first()
    if wishlist_status:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})


def remove_from_wishlist(request, buyer_id, product_id):
    buyer = models.Buyer.objects.filter(id=buyer_id).first()
    product = models.Product.objects.filter(id=product_id).first()
    remove_from_wishlist = models.Wishlist.objects.filter(
        buyer=buyer, product=product
    ).delete()
    if remove_from_wishlist:
        return JsonResponse({"bool": True})
    else:
        return JsonResponse({"bool": False})
