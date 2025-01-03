from django.shortcuts import render
from django.http import *
from owner.models import *
from office.models import *
from django.template.loader import *
from django.db.models import Avg, Sum, Min, Max
# Create your views here.

def search_item_by_category(request):
    if request.method == 'GET':
        c_id = request.GET['c_id']
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile, status=1).first()
        item_id = []
        for i in Select_category_item.objects.filter(category_id=c_id):
            item_id.append(i.item_id)
        context={
                'e':e,
                'item':Item.objects.filter(id__in=item_id)
        }
        t = render_to_string('ajax/search_item.html', context) 
    return JsonResponse({'t': t})

def search_item(request):
    if request.method == 'GET':
        words = request.GET['words']
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile, status=1).first()
        context={
                'item':Item.objects.filter(shope_id=e.shope_id,name__icontains=words)[:3],
                'e':e
        }
        t = render_to_string('ajax/search_item.html', context) 
    return JsonResponse({'t': t})

def add_item_to_cart(request):
    if request.method == 'GET':
        employee_id = request.GET['employee_id']
        item_id = request.GET['item_id']
        price = request.GET['price']
        qty = request.GET['qty']
        total_amount = request.GET['total_amount']
        e = office_employee.objects.filter(id=employee_id).first()

        c = Cart.objects.filter(office_employee_id=employee_id, item_id=item_id).first()
        if c:
            c.qty = qty
            c.price = price
            c.total_amount = total_amount
            c.save()
        else:
            Cart(
                shope_id=e.shope_id,
                office_employee_id=employee_id,
                item_id = item_id,
                price=price,
                qty=qty,
                total_amount=total_amount
            ).save()
        amount = Cart.objects.filter(office_employee_id=employee_id).aggregate(Sum('total_amount'))
        amount = amount['total_amount__sum']
        context={
                'cart':Cart.objects.filter(office_employee_id=employee_id),
        }
        t = render_to_string('ajax/item_to_cart.html', context) 
    return JsonResponse({'t': t,'amount':amount})

def cut_item_to_cart(request):
    if request.method == 'GET':
        employee_id = request.GET['employee_id']
        item_id = request.GET['item_id']
        price = request.GET['price']
        qty = request.GET['qty']
        total_amount = request.GET['total_amount']
        e = office_employee.objects.filter(id=employee_id).first()
        
        c = Cart.objects.filter(office_employee_id=employee_id, item_id=item_id).first()
        if int(qty) == 0:
            Cart.objects.filter(office_employee_id=employee_id, item_id=item_id).delete()
        else:
            c.qty = qty
            c.price = price
            c.total_amount = total_amount
            c.save()
        amount = Cart.objects.filter(office_employee_id=employee_id).aggregate(Sum('total_amount'))
        amount = amount['total_amount__sum']
        context={
                'cart':Cart.objects.filter(office_employee_id=employee_id),
        }
        t = render_to_string('ajax/item_to_cart.html', context) 
    return JsonResponse({'t': t,'amount':amount})

def select_category_item(request):
    if request.method == 'GET':
        shope_id = request.GET['shope_id']
        category_id = request.GET['category_id']
        item_id = request.GET['item_id']
        s = Select_category_item.objects.filter(item_id=item_id,category_id=category_id).first()
        if s:
            if s.status == 1:
                status = 0
                s.status = 0
                s.save()
            else:
                status = 1
                s.status = 1
                s.save()
        else:
            status = 1
            Select_category_item(
                shope_id=shope_id,
                item_id=item_id,
                category_id=category_id
            ).save()
        return JsonResponse({'status': status})