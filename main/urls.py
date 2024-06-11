from django.urls import path
from main.views import index, about, contact, prices, ayuda, success, private

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('success/', success),    
    path('private/', private),    
]