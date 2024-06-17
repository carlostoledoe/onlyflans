from django.urls import path
from main.views import index, about, contact, prices, ayuda, success, welcome, register, pruebas, suscriptions, registerfree, registerpremium, registerdiamond

urlpatterns = [
    path('', index),
    path('about/', about),
    path('contact/', contact),
    path('prices/', prices),
    path('ayuda/', ayuda),
    path('success/', success),    
    path('welcome/', welcome),    
    path('accounts/register/', register, name='register'), 
    path('pruebas/', pruebas, name='pruebas' ),
    path('suscriptions/', suscriptions, name ='suscriptions'),
    #path('registerfree/', registerfree, name ='registerfree'),
    path('registerpremium/', registerpremium, name ='registerpremium'),
    path('registerdiamond/', registerdiamond, name ='registerdiamond'),
] 