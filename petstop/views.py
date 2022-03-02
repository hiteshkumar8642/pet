from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Pet,Item,User_Detail
# Create your views here.
def home(request):
        return render(request,'index.html')
def pshop(request):
        return render(request,'pshop.html')
def pcheckout(request):
        return render(request,'pcheckout.html')
def ishop(request):
        return render(request,'ishop.html')
def item(request):
        return render(request,'item.html')
def icheckout(request):
        return render(request,'icheckout.html')
def sign_in(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=auth.authenticate(username=uname,password=password)
        if user is None:
            return redirect('sign_up')
        if user is not None:
            auth.login(request,user)
            return redirect('home')
    else:
        return render(request,'sign_in.html')
def logout(request):
    auth.logout(request)
    return redirect('sign_in')
def sign_up(request):
    if request.method=='POST':
        uname=request.POST['uname']
        password1=request.POST['password1']
        password2=request.POST['password2']

        user=User.objects.create_user(username=uname,password=password1)
        user.save()
        print('user created')
        return redirect('home')
    else:
        return render(request,'sign_up.html')
