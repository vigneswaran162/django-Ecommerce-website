from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse 
import json

def index(request):
    products=product.objects.filter(trending=1)   
    return render(request,'shop/index.html',{"products":products})
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
       if request.user.is_authenticated:
           data=json.load(request)
           product_qty=data['product_qty']
           product_id=data['pid']
           product_status=product.objects.get(id=product_id)
           if product_status:
               if cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':' Product  Already in  Cart'},status=200)
               else:
                   if product_status.quantity >= product_qty:
                      cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                      return JsonResponse({'status':'Product  Added to Cart'},status=200)
                   else:
                      return JsonResponse({'status':'Product Stock not Available'},status=200)

       else:
           return JsonResponse({'status':'login to add to cart'},status=200)
        
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
    

    
def signup(request):
    if request.method=='POST':
       user = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       if User.objects.filter(username=user).exists():
           messages.success(request, 'username already exists')
       else:
           u = User.objects.create_user(username=user,email=email,password=password)
           u.save()
           return redirect('login')  
    return render(request,'shop/signup.html')

def login_page(request):
    if request.user.is_authenticated:
          return redirect('home')
    else:
     if request.method == 'POST':
       name = request.POST.get('username')
       password = request.POST.get('password')
       user=authenticate(request,username=name,password=password)
       if user is not None:
           login(request,user)
           return redirect('home')
       else:
           messages.error(request,'incorrect username or password')
           return redirect('login')
           
    return render(request,'shop/login.html')

def logout_page(request):
    if request.user.is_authenticated:
       logout(request)    
       return redirect('home')

def category(request):
    cat = catagory.objects.filter(status=0)
    return render(request,'shop/category.html',{"cat":cat})
def categoryview(request,name):
    if(catagory.objects.filter(name=name,status=0)):
        products = product.objects.filter(category__name=name)
        return render(request,'shop/products.html',{"products":products,"category_name":name})
    else:
       messages.warning(request,"no such category found")
       
def product_details(request,cname,pname):
    if(catagory.objects.filter(name=cname,status=0)):
      if(product.objects.filter(name=pname,status=0)):
          products= product.objects.filter(name=pname,status=0).first()
          return render(request,'shop/product_details.html',{"products":products})
      else:
         messages.warning(request,"no such products found")
    else:
       return redirect('category') 
   
    

def cart_page(request):
    if request.user.is_authenticated:
        c = cart.objects.filter(user=request.user)
        return render(request,"shop/cart.html",{"c":c})
    else:
        return redirect('/')
    
def remove_cart(request,cid):
    cartitem = cart.objects.get(id=cid)
    cartitem.delete()
    return redirect('cart') 