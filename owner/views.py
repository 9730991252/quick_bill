from django.shortcuts import render, redirect
from sunil.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import math
# Create your views here.
def owner_home(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        context={
            'shope':shope
        }
        return render(request, 'owner/owner_home.html', context)
    else:
        return redirect('login')
     
def add_employee(request):
    if request.session.has_key('owner_mobile'):
        mobile = request.session['owner_mobile']
        shope = Shope.objects.filter(mobile=mobile).first()
        if 'Add_employee'in request.POST:
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if office_employee.objects.filter(mobile=mobile).exists():
                pass
            else:
                office_employee(
                    shope_id=shope.id,
                    name=name,
                    mobile=mobile,
                    pin=pin,
                ).save()    
            return redirect('/owner/add_employee/')
        if 'Edit_employee'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            office_employee(
                id=id,
                shope_id=shope.id,
                name=name,
                mobile=mobile,
                pin=pin,
            ).save()
            return redirect('/owner/add_employee/')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = office_employee.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('/owner/add_employee/')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = office_employee.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('/owner/add_employee/')
        
        context={
            'shope':shope,
            'office_employee':office_employee.objects.filter(shope_id=shope.id)
        }
        return render(request, 'owner/add_employee.html', context)
    else:
        return redirect('login')
    
