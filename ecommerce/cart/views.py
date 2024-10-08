from django.shortcuts import render, get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render (request, "cart_summary.html",{"cart_products":cart_products})

def cart_add(request):
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #get the post
        product_id = int(request.POST.get('product_id'))
        #look for product
        product = get_object_or_404(Product, id=product_id)
        #save session
        cart.add(product=product)

        response = JsonResponse({'Product Name': ':product.name'})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass