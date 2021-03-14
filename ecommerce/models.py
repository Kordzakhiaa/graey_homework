from django.db import models

from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Category title'))
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['order']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=150, verbose_name=_('Product name'))
    slug = models.SlugField(max_length=150)  # @TODO what is slug :d
    price = models.DecimalField(decimal_places=4, max_digits=8)
    description = models.TextField()
    is_published_date = models.DateTimeField(auto_now_add=True)
    is_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    category = models.ManyToManyField(Product)
    title = models.CharField(max_length=150, verbose_name=_('Tag title'))

    def __str__(self):
        return self.title


class Cart(models.Model):
    owner = models.OneToOneField(to='user.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.owner


class CartItem(models.Model):
    category = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    active = models.BooleanField()
