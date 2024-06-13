from django.urls import path
from main.views import index, about, contact, prices, ayuda, success, welcome, register, logout_view

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('success/', success),    
    path('welcome/', welcome),    
    # path('login/', login),     
    path('register/', register), 
    path('logout/', logout_view, name='logout'),    
]