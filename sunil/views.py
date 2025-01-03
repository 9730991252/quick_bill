from django.shortcuts import redirect, render
from . models import *
# Create your views here.
def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["number"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 11000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_home')
        else:
            return redirect('sunil_login')
    return render(request, 'sunil/sunil_login.html')


def sunil_home(request):
    if request.session.has_key('sunil_mobile'):
        if 'Add_shope'in request.POST:
            shope_name = request.POST.get('shope_name')
            owner_name = request.POST.get('owner_name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            if Shope.objects.filter(mobile=mobile).exists():
                pass
            else:
                Shope(
                    shope_name=shope_name,
                    owner_name=owner_name,
                    mobile=mobile,
                    pin=pin,
                ).save()    
            return redirect('sunil_home')
        if 'Edit_shope'in request.POST:
            id = request.POST.get('id')
            shope_name = request.POST.get('shope_name')
            owner_name = request.POST.get('owner_name')
            mobile = request.POST.get('mobile')
            pin = request.POST.get('pin')
            Shope(
                id=id,
                shope_name=shope_name,
                owner_name=owner_name,
                mobile=mobile,
                pin=pin,
            ).save()
            return redirect('sunil_home')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Shope.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('sunil_home')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Shope.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('sunil_home')
        context={
            'shope':Shope.objects.all()
        }
        return render(request, 'sunil/sunil_home.html', context)
    else:
        return redirect('sunil_login')