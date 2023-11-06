from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render(request,"index.html")

def user_register(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        
        useri= User.objects.create_user(
             username=uname,
             password=passw,
             is_custumer=True,
        )
        return redirect('index')
    else:
        return render(request,"user_register.html")

def user_login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        
        useri=User.objects.filter(username=uname).first()
        
        if useri is not None and useri.check_password(passw) and useri.is_custumer:
            
            login(request,useri)
            return redirect('user_home')
        else:
            
            messages.error(request,'invalid')
            
    return render(request,"user_login.html")


    
def user_home(request):
    
    return render(request,"user_home.html")

def sign_out(request):
    logout(request)
    return redirect('index')

def mess_register(request):
    if request.method=="POST":
        mname=request.POST.get('username')
        passi=request.POST.get('password')
        
        messi= User.objects.create_user(
             username=mname,
             password=passi,
             is_mess=True,
        )
        return redirect('index')
    else:
        return render(request,"mess_register.html")
    
def mess_login(request):
    if request.method=='POST':
        mname=request.POST.get('username')
        passi=request.POST.get('password')
        
        messi=User.objects.filter(username=mname).first()
        
        if messi is not None and messi.check_password(passi) and messi.is_mess:
            
            login(request,messi)
            return redirect('mess_home')
        else:
            
            messages.error(request,'invalid')
            
    return render(request,"mess_login.html")

def mess_home(request):
    
    return render(request,"mess_home.html")
