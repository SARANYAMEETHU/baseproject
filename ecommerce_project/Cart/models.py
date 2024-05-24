from django.db import models
from shop.models import PRODUCT


# Create your models here.
class CART(models.Model):
    objects = None
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'CART'
        ordering = ['date_added']

    def __str__(self):
        return '{}'.format(self.cart_id)


class CARTITEM(models.Model):
    objects = None
    product = models.ForeignKey(PRODUCT, on_delete=models.CASCADE)
    cart = models.ForeignKey(CART, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CARTITEM'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return '{}'.format(self.product)
