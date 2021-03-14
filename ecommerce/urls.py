from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce.views import ProductListView, CategoryView, ProductCreateView

app_name = 'ecommerce'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('category/', CategoryView.as_view(), name='category_list'),
]

# router = DefaultRouter()
# router.register(r'product_detail', ProductListView, basename='products')
# urlpatterns = router.urls
