from django.db import models
from sunil.models import *
from owner.models import *
# Create your models here.
class Item(models.Model):
    shope = models.ForeignKey(Shope, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    status = models.IntegerField(default=1) 
    
class Cart(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    office_employee = models.ForeignKey(office_employee,on_delete=models.PROTECT,null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    price = models.FloatField()
    total_amount = models.FloatField(default=0)
    qty = models.IntegerField()
    
class OrderMaster(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    office_employee = models.ForeignKey(office_employee,on_delete=models.PROTECT,null=True)
    total_price=models.FloatField(default=0,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    order_filter=models.IntegerField(default=True)
    
    
class OrderDetail(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    office_employee = models.ForeignKey(office_employee,on_delete=models.PROTECT,null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    qty = models.IntegerField(default=1)
    price=models.FloatField(default=0,null=True)
    total_price=models.FloatField(default=0,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    order_filter=models.IntegerField(default=True)

class Category(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    
class Select_category_item(models.Model):
    shope = models.ForeignKey(Shope,on_delete=models.PROTECT,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True)
    item = models.ForeignKey(Item,on_delete=models.PROTECT,null=True)
    status = models.IntegerField(default=1)