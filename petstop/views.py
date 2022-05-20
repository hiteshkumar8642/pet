from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Pet,Item,User_Detail,Cart,Post
from django.core import serializers
# Create your views here.
def home(request):
        return render(request,'index.html')
def pshop(request):
        objs =Post.objects.all()
        res = []
        for x in objs:
            res.append({
                "sku":x.id,
                "product":x.pet_id.pet_name,
                "image": x.pet_id.pet_pic.url,
                "description": x.pet_id.description,
                "details": x.description,
                "price": x.price
            })
        res.append({
            "checkoutBool": False,
            "cart": [],
            "cartSubTotal": 0,
            "tax": 0.065,
            "cartTotal": 0
        })
        print(res)
        # data = serializers.serialize("json",res)
        with open('new_file.json', 'w') as f:
            json.dump(res, f, indent=2)
            print("New json file is created from data.json file")
        context = {'productsData': res}
        print(context)
        return render(request,'pshop.html')#for context add , context after name of html file
def pcheckout(request):
        return render(request,'pcheckout.html')
def pet(request):
        objs =Pet.objects.all()
        return render(request,'pet.html',{'objs':objs})
def ishop(request):
        objs =Item.objects.all()
        return render(request,'ishop.html',{'objs':objs})
def item(request):
    if request.method=='POST' and 'upload' in request.FILES:
         name=request.POST['name']
         upload = request.FILES['upload']
         cost_price=request.POST['cost_price']
         color=request.POST['color']
         qty=request.POST['qty']
         quan=int(qty)
         if quan<0:
             messages.warning(request, 'Item quantity cannot be less than zero!')
             return redirect('item')
         qty_type=request.POST['qty_type']
         des=request.POST['des']
         item=Item(item_name=name,mrp=cost_price,quantity=qty,type=qty_type,color=color,description=des,item_pic=upload)
         item.save()
         print('item saved')
         return redirect('item')
    else:

        if request.user.is_authenticated:
            objs =Item.objects.all()
            return render(request,'item.html',{'objs':objs})
        else:
            return redirect('/')
def icheckout(request):
        return render(request,'icheckout.html')
def tracker(request):
        return render(request,'tracker.html')
def cart(request):
        if request.user.is_authenticated:
            objs =Cart.objects.filter(user=request.user)
            tot=0
            for x in objs:
                tot= tot+x.item.mrp*x.quantity
            tax=tot*5/100
            net_tot=tot+tax + 15.00
            price={"tot":tot,"tax":tax,"net_tot":net_tot}
            return render(request,'cart.html',{'objs':objs,"price":price})
        else:
           return redirect('sign_in')
def aboutus(request):
        return render(request,'aboutus.html')
def contactus(request):
        return render(request,'contactus.html')
def faq(request):
        return render(request,'faq.html')
def tq(request):
        return render(request,'tq.html')
def cartadd(request,item_id):
    if request.method=='GET':
        c_user=request.user
        cart=Cart(item_id=item_id,quantity=1,discount=0,user=c_user)
        cart.save()
        print('Added to cart')
        return redirect('ishop')
def cartremove(request,item_id):
    if request.method=='GET':
        c_user=request.user
        item=Cart.objects.get(id=item_id,user=c_user)
        item.delete()
        print('item deleted')
        return redirect('cart')
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
    return redirect('/')
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
