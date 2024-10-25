from django.urls import path
from . import views

urlpatterns = [
  #  path('shipping_info', views.shipping_info, name="shipping_info"),
    path('success/', views.success, name='success'), 
    path('checkout/', views.checkout, name='checkout'), 
    path('order_item/', views.order_item, name='order_item'), 




]