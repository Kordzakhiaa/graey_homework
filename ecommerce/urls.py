from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce.views import ProductListView, CategoryView, CartListView, CartItemViewSet, AddToCartView

app_name = 'ecommerce'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryView.as_view(), name='category_list'),
    path('cart_list/', CartListView.as_view(), name='cart_list'),
]
router = DefaultRouter()

router.register('cart_items', CartItemViewSet, basename='cart_item')
router.register('to_cart', AddToCartView, basename='add_to_cart')

urlpatterns += router.urls
