from django.urls import path
from . import views

urlpatterns = [
  #  path('shipping_info', views.shipping_info, name="shipping_info"),
    path('success/', views.success, name='success'), 
    path('checkout/', views.checkout, name='checkout'), 



]