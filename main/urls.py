from django.urls import path
from main.views import index, about, welcome, prices, ayuda, contact_form

urlpatterns = [
    path('', index),
    path('about/', about),
    path('welcome/', welcome),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('contact_form', contact_form, name='contact_form')
]