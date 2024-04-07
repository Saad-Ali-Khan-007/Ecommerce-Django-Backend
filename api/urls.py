from django.urls import path

from . import views


urlpatterns = [
    # Seller
    # Seller Post and Get
    path("seller/", views.SellerList.as_view()),
    # Individual Seller Delete, Update And Retrieve
    path("seller/<int:pk>", views.SellerDetail.as_view()),
    # Product
    # Product Category Post and Get
    path("product-category/", views.ProductCategoryList.as_view()),
    # Product Post and Get
    path("product/", views.ProductList.as_view()),
    # Individual Product Delete And Retrieve
    path("product/<int:pk>", views.ProductDetail.as_view()),
    # Buyer
    # Buyer Post and Get
    path("buyer/", views.BuyerList.as_view()),
    # Rating
    # Buyer POST And GET rating and review
    path("rating-review/", views.RatingReviewList.as_view()),
    # Individual Product Rating and Review
    path("product-rating-review/<int:product_id>", views.RatingReviewList.as_view()),
    # Buyer rating status(given or not)
    path("rating-status/<int:buyer_id>/<int:product_id>", views.buyerRatingStatus),
]
