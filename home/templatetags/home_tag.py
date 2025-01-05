from django import template
from owner.models import *
from django.db.models import Avg, Sum, Min, Max
from math import *
import math
from datetime import date
from office.models import *
register = template.Library()

@register.simple_tag()
def cart_item_detail(item_id, employee_id):
    cart = Cart.objects.filter(item_id=item_id,office_employee_id=employee_id).first()
    if cart:
        return {'qty':cart.qty, 'amount':cart.total_amount}
    else:
        return {'qty':0, 'amount':0}
    
@register.simple_tag()
def edit_cart_item_detail(item_id, order_filter):
    o = OrderDetail.objects.filter(item_id=item_id,order_filter=order_filter).first()
    if o:
        return {'qty':o.qty, 'amount':o.total_price}
    else:
        return {'qty':0, 'amount':0}
    
@register.simple_tag()
def todayes_total_amount(shope_id):
    t =  OrderMaster.objects.filter(shope_id=shope_id,ordered_date__icontains=date.today()).aggregate(Sum('total_price'))
    t =  t['total_price__sum']
    if t:
        return t
    else:
        return 0
        
# @register.inclusion_tag('inclusion_tag/office/pendding_completed_farmer_bill.html')
# def pendding_completed_farmer_bill(farmer_id):
#     if farmer_id:
#         farmer_bill = Farmer_bill.objects.filter(farmer_id=farmer_id)
#         total_amount = farmer_bill.aggregate(Sum('total_amount'))
#         total_amount = total_amount['total_amount__sum']
#         print(total_amount)
        