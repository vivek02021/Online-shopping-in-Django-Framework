from django.shortcuts import render,HttpResponse,redirect
from .models import Category,Product
def home(request):
    cl=Category.objects.all()
    pl=Product.objects.all()
    d={'cl':cl,'pl':pl}
    return render(request,'home.html',d)

def get_by_category(request,id):
    cl=Category.objects.all()
    pl=Product.objects.filter(category=id)
    d={'cl':cl,'pl':pl}
    return render(request,'home.html',d)

def search_product(request):
    cl=Category.objects.all()
    pl=Product.objects.all()

    if request.method=='POST':
        name=request.POST.get('srch')
        pl=Product.objects.filter(name__contains=name)
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
    
    else:
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)

from .forms import UserForm
def addUser(request):
    cl=Category.objects.all()
    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        d={'cl':cl}
        return redirect('/')

    else:
        f=UserForm
        d={'cl':cl,'form':f}
        return render(request,'form.html',d)

from django.contrib.auth import login,logout,authenticate
def login_view(request):
    cl=Category.objects.all()
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("InValid userName or password")

    else:
     
        d={'cl':cl}
        return render(request,'login.html',d)


def logout_view(request):
    logout(request)
    return redirect('/')

from django.contrib.auth.models import User
from .models import Cart,Order
def addtocart(request,id):
    prd=Product.objects.get(id=id)
    uid=request.session.get('uid')    
    user=User.objects.get(id=uid)
    crt=Cart()
    crt.product=prd
    crt.user=user
    crt.save()
    return redirect('/')

def cart_list(request):
    uid=request.session.get('uid')  
    if request.method=='POST':
        mord=Order()
        bill=request.POST.get('bill')
        user=User.objects.get(id=uid)
        mord.totalBill=bill
        mord.user=user
        mord.save()
        crlist=Cart.objects.filter(user=uid)
        for c in crlist:
            c.delete()
        return redirect('/')
    else:
       
        cl=Category.objects.all()
        crlist=Cart.objects.filter(user=uid)
        
        totalBill=0
        for i in crlist:
            totalBill=totalBill+i.product.price
    
        d={'cl':cl,'crlist':crlist,'totalBill':totalBill}
        return render(request,'cartlist.html',d)


def my_order(request):
    cl=Category.objects.all()
    uid=request.session.get('uid')
    orlist=Order.objects.filter(user=uid)
    d={'cl':cl,'orlist':orlist}
    return render(request,'orderlist.html',d)
