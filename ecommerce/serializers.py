from rest_framework import serializers

from ecommerce.models import Cart, Tag, Product, Category


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


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = [
            'id',
            'owner',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title',
        ]
