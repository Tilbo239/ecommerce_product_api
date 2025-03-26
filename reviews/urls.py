from django.urls import path
from .views import CreateReview, ProductReviewList, ReviewList, ReviewDetail


urlpatterns = [
    path("products/<int:pk>/reviews/new/", CreateReview.as_view(), name="new-review"),
    path("products/<int:pk>/reviews/", ProductReviewList.as_view(), name="product-reviews"),
    path("reviews/", ReviewList.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]