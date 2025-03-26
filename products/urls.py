from django.urls import path, include
from .views import ( ProductImageViewSet, ProductViewSet, CategoryViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"products", ProductViewSet, basename="product")
router.register(r"product-image", ProductImageViewSet, basename="image")

 

urlpatterns = [
    path("", include(router.urls)),
]