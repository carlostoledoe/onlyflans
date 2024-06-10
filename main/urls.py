from django.urls import path
from main.views import index, about, welcome, prices, ayuda, success, private

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('success/', success),    
    path('private/', private),    
]