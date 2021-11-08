from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    stock_pcs = models.PositiveIntegerField()
    price = models.FloatField()
    shop_id = models.CharField(max_length=10)
    vip = models.BooleanField()

    def __str__(self):
        return f'product_id = {self.product_id}; stock_pcs = {self.stock_pcs}; price = {self.price}; shop_id = {self.shop_id}; vip = {self.vip}'


class Order(models.Model):
    product_id = models.ForeignKey('Product', on_delete=SET_NULL, null=True)
    gty = models.PositiveIntegerField()
    price = models.FloatField()
    shop_id = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        des = f'order_id = {self.id}; product_id = {self.product_id}; gty = {self.gty}; price = {self.price}; shop_id = {self.shop_id}'
        return des
