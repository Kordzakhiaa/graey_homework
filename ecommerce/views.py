from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from ecommerce.models import Product, Category
from ecommerce.serializers import ProductListSerializer, CategoryListSerializer
from rest_framework import generics, status, filters


class ProductListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    filter_fields = ['category', 'price']
    lookup_field = ['slug']
    # filterset_class = ProductFilter


class CategoryView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class ProductCreateView(generics.ListCreateAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = [filters.SearchFilter]

    queryset = Product.objects.all()
    search_fields = ['title']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
