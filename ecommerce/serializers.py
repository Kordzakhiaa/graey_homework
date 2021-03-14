from django.db.models import F, Sum, DecimalField
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
    product = serializers.ReadOnlyField(source='product.title')

    class Meta:
        model = CartItem
        fields = [
            'product',
            'cart',
            'quantity',
        ]


class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    total_cost = serializers.SerializerMethodField(method_name='get_total_cost')

    def get_total_cost(self, obj):  # noqa
        total_price = CartItem.objects.filter(active=True).aggregate(
            total_price=Sum((F('product__price') * F('quantity')), output_field=DecimalField())).get('total_price')

        return total_price

    class Meta:
        model = Cart
        fields = [
            'items',
            'total_cost',
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title',
        ]


class AddToCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']
