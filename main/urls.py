from django.urls import path
from main.views import index, about, welcome, prices, ayuda

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('prices/', prices),
    path('ayuda/', ayuda),
]