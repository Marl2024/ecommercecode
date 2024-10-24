from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    path('search_items/', views.search_items, name='search_items'),

   
]