from django.shortcuts import render, redirect
from sunil.models import *
from owner.models import *
from django.views.decorators.csrf import csrf_exempt
import math
from django.db.models import Avg, Sum, Min, Max
from django.contrib import messages 
from .models import *
from   datetime import date
# Create your views here.
@csrf_exempt
def office_home(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
            amount = Cart.objects.filter(shope_id=e.shope_id,office_employee_id=e.id).aggregate(Sum('total_amount'))
            amount = amount['total_amount__sum']
            if amount == None:
                amount = 0
            if 'Delete'in request.POST:
                cart_id = request.POST.get('cart_id')
                Cart.objects.filter(id=cart_id).delete()
                return redirect('office_home')
            if 'complete_order'in request.POST:
                amount = Cart.objects.filter(shope_id=e.shope_id,office_employee_id=e.id).aggregate(Sum('total_amount'))
                amount = amount['total_amount__sum']
                order_filter = OrderMaster.objects.filter(shope_id=e.shope_id).count()
                order_filter += 1
                OrderMaster(
                    shope_id=e.shope_id,
                    office_employee_id = e.id,
                    total_price=amount,
                    order_filter=order_filter
                ).save()
                om = OrderMaster.objects.filter(shope_id=e.shope_id,order_filter=order_filter).first()
                cart = Cart.objects.filter(shope_id=e.shope_id,office_employee_id=e.id)
                if cart:
                    for c in cart:
                        OrderDetail(
                            shope_id=e.shope_id,
                            office_employee_id = e.id,
                            item_id=c.item_id,
                            qty=c.qty,
                            price=c.price,
                            total_price=c.total_amount,
                            order_filter=order_filter,
                        ).save()
                Cart.objects.filter(shope_id=e.shope_id,office_employee_id=e.id).delete()
                return redirect(f'/office/completed_view_bill/{order_filter}')
        context={
            'e':e,
            'cart':Cart.objects.filter(shope_id=e.shope_id,office_employee_id=e.id),
            'item':Item.objects.filter(shope_id=e.shope_id,status=1),
            'amount':amount,
            'category':Category.objects.filter(shope_id=e.shope_id,status=1).order_by('-order_by'),
        }
        return render(request, 'office/office_home.html', context)
    else:
        return redirect('login')
    
def select_category_items(request,category_id):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
            item = []
            for i in Item.objects.filter(shope_id=e.shope_id):
                selected_status = 0
                if Select_category_item.objects.filter(item_id=i.id,category_id=category_id,status = 1):
                    selected_status = 1 
                print(selected_status)
                item.append({'name':i.name, 'selected_status':selected_status ,'id':i.id})
        context={
            'e':e,
            'item':item,
            'category':Category.objects.filter(id=category_id).first(),
        }
        return render(request, 'office/select_category_items.html', context)
    else:
        return redirect('login')
    
def completed_bill(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile, status=1).first()
        context={
            'e':e,
            'bill':OrderMaster.objects.filter(shope_id=e.shope_id).order_by('-id')[0:500],
        }
        return render(request, 'office/completed_bill.html', context)
    else:
        return redirect('/login/')
    
def completed_view_bill(request,order_filter):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if e:
            o = OrderDetail.objects.filter(order_filter=order_filter).aggregate(Sum('total_price'))
        context={
            'e':e,
            'order_master':OrderMaster.objects.filter(shope_id=e.shope_id,order_filter=order_filter).first(),
            'order_detail':OrderDetail.objects.filter(shope_id=e.shope_id,order_filter=order_filter),
            'shope':Shope.objects.filter(id=e.shope_id).first(),
            'total_amount':o['total_price__sum'],
        }
        return render(request, 'office/completed_view_bill.html', context)
    else:
        return redirect('/login/')
    
def category(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if 'add_category'in request.POST:
            name = request.POST.get('name')
            Category(
                shope_id=e.shope_id,
                name=name,
            ).save()
            return redirect('category')
        if 'edit_category'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            i = Category.objects.filter(id=id).first()
            i.name = name
            i.save()
            return redirect('category')
        if 'active'in request.POST:
            id = request.POST.get('id')
            i = Category.objects.filter(id=id).first()
            i.status = 0
            i.save()
            return redirect('category')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            i = Category.objects.filter(id=id).first()
            i.status = 1
            i.save()
            return redirect('category')
        if 'save_order_by'in request.POST:
            c_id = request.POST.get('id')
            order_by = request.POST.get('order_by')
            c = Category.objects.filter(id=c_id).first()
            c.order_by = order_by
            c.save()
            return redirect('category')
               
        context={
            'e':e,
            'category':Category.objects.filter(shope_id=e.shope_id).order_by('-order_by'),
        }
        return render(request, 'office/category.html', context)
    else:
        return redirect('login')
    
def item(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile).first()
        if 'add_item'in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            Item(
                shope_id=e.shope_id,
                name=name,
                price=price
            ).save()
            return redirect('item')
        if 'edit_item'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            price = request.POST.get('price')
            c = Item.objects.filter(id=id).first()
            c.name = name
            c.price = price
            c.save()
            return redirect('item')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Item.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('item')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Item.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('item')   
        context={
            'e':e,
            'item':Item.objects.filter(shope_id=e.shope_id),
        }
        return render(request, 'office/item.html', context)
    else:
        return redirect('login')

def profile(request):
    if request.session.has_key('office_mobile'):
        m = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=m).first()
        if 'edit_profile'in request.POST:
            shope_name = request.POST.get('shope_name')
            address = request.POST.get('address')
            contact_details = request.POST.get('contact_details')
            
            s = Shope.objects.filter(id=e.shope_id).first()
            s.shope_name = shope_name
            s.address = address
            s.contact_details = contact_details
            s.save()
            
            ##
            
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            
            del request.session['office_mobile']
            request.session['office_mobile'] = request.POST.get('mobile')
            
            e.name = name
            e.mobile = mobile
            e.pin = pin
            e.save()
            return redirect('profile')
        context={
            'e':e,
        }
        return render(request, 'office/profile.html', context)
    else:
        return redirect('login')
    
def report(request):
    if request.session.has_key('office_mobile'):
        mobile = request.session['office_mobile']
        e = office_employee.objects.filter(mobile=mobile, status=1).first()
        item = []
        from_date = ''
        to_date = ''
        total_amount = 0
        if 'search_report' in request.POST:
            from_date = request.POST['from_date']
            to_date = request.POST['to_date']
            total_amount = 0
            for i in Item.objects.filter(shope_id=e.shope_id):
                qty = OrderDetail.objects.filter(item_id=i.id,date__range=[from_date, to_date] ).aggregate(Sum('qty'))['qty__sum']
                total_price = OrderDetail.objects.filter(item_id=i.id, date__range=[from_date, to_date]).aggregate(Sum('total_price'))['total_price__sum']
                if total_price == None:
                    total_price = 0
                total_amount += total_price
                if qty != None:
                    item.append({'name':i.name, 'qty':qty, 'total_price':total_price})        
        context={
            'e':e,
            'item':item,
            'from_date':from_date,
            'to_date':to_date,
            'total_amount':total_amount,
        }
        return render(request, 'office/report.html', context)
    else:
        return redirect('/login/')