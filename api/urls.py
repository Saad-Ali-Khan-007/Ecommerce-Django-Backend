from django.urls import path

from . import views


urlpatterns = [
    # Seller
    # Seller Post and Get
    path("seller/", views.SellerList.as_view()),
    # Individual Seller Delete, Update And Retrieve
    path("seller/<int:pk>", views.SellerDetail.as_view()),
    # Product Category Post and Get
    path("product-category/", views.ProductCategoryList.as_view()),
    # Product
    # Product Post and Get
    path("product/", views.ProductList.as_view()),
    # Individual Product Delete And Retrieve
    path("product/<int:pk>", views.ProductDetail.as_view()),
]
