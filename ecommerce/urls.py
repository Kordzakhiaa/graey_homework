from django.urls import path

from ecommerce.views import ProductListView

app_name = 'ecommerce'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
]
