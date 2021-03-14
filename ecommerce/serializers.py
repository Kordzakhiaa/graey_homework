from rest_framework import serializers

from ecommerce.models import Cart, Tag, Product, Category, CartItem


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'slug',
            'price',
            'description',
            'category',
        ]


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('category',)


class CartItemSerializer(serializers.ModelSerializer):
    price = serializers.CharField(source='product.price', read_only=True)

    class Meta:
        model = CartItem
        field = [
            'product',
            'cart',
            'quantity',
        ]
    # @TODO: Filter by active carts


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title',
        ]
