from django.db import models

# Create your models here.
from users.models import CustomUser


class Order(models.Model):
    deliver=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="orders", blank=True, null=True)
    full_name=models.CharField(max_length=512, verbose_name='Client name')
    phone=models.CharField(max_length=9, verbose_name='Client phone number')
    from_address = models.CharField(max_length=512, verbose_name='From address')
    to_address = models.CharField(max_length=512, verbose_name='To address')
    landmark = models.CharField(max_length=512, verbose_name='Orientir')
    created_at = models.DateField(auto_now_add=True, verbose_name='Order created', editable=False)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Orders'
        db_table = 'order'

class OrderItem(models.Model):
        order_id=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", blank=True, null=True)
        product_id =  models.IntegerField(verbose_name='Product id')
        price = models.DecimalField(max_digits=6, decimal_places=2)

        class Meta:
            verbose_name_plural = 'OrderItems'
            db_table = 'order_items'
            ordering = ['-pk']
