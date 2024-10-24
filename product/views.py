from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse



from.forms import SignUpForm
from django import forms

def search_items(request):
    query = request.GET.get('q', '')
    if query:
        # Check if the query is a number (for ID search)
        if query.isdigit():
            products = Product.objects.filter(id=query)
        else:
            products = Product.objects.filter(name__icontains=query)
        
        products_list = [{'id': product.id, 'name': product.name} for product in products]
        return JsonResponse(products_list, safe=False)
    
    return JsonResponse([], safe=False)





def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products':products})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in!"))
            return redirect('home')
        
        else:
            messages.success (request,("Please logged in!"))
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')




def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password= password )
            login(request,user)
          #  messages.success(request, ("You have registered"))
            return redirect ('home')
        else:
          #  messages.success(request, ("Try to register "))
            return redirect ('register')
  
    else:
        return render(request, 'register.html', {'form': form})