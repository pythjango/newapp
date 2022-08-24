from django.shortcuts import render
def seller_home(request):
    return render (request,'seller/home.html')
def seller_cart(request):
    return render (request,'seller/cart.html')  
def seller_order(request):
    return render (request,'seller/order.html')        

# Create your views here.
