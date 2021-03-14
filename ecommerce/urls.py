from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce.views import ProductListView, CategoryView, CartListView, CartItemViewSet

app_name = 'ecommerce'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('category/', CategoryView.as_view(), name='category_list'),
    path('cart_list/', CartListView.as_view(), name='cart_list'),
]
router = DefaultRouter()

router.register('cart_items', CartItemViewSet)

urlpatterns += router.urls
