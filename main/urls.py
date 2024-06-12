from django.urls import path
from main.views import index, about, contact, prices, ayuda, success, welcome, login, register

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('success/', success),    
    path('welcome/', welcome),    
    path('login/', login),     
    path('register/', register),     
]