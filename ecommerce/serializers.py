from rest_framework import serializers

from ecommerce.models import Cart, Tag, Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            # 'category',
            'title',
            'slug',
            'price',
            'description',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']