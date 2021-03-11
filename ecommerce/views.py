from rest_framework.response import Response

from ecommerce.filters import ProductFilter
from ecommerce.models import Product
from ecommerce.serializers import ProductSerializer
from rest_framework import generics, status, filters


class ProductListView(generics.ListAPIView):
    # permission_classes =
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    filter_fields = ['category', 'price']
    # filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset
