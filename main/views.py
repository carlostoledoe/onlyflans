from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import Contact, Flan

import json
import os

# Create your views here.
def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'index.html', context)

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    context = {'flanes': flanes_privados}
    return render(request, 'welcome.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'GET':
        form = ContactForm()                    # Se crea una instancia del formulario ContactForm sin datos iniciales.
        context = {'form': form}                # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'contact.html', context) # Se renderiza la plantilla 'contact.html' con el contexto.
    else:
        form = ContactForm(request.POST)        # Se crea una instancia de ContactForm con los datos enviados en la solicitud POST.
        if form.is_valid():                     # Se verifica si los datos del formulario son válidos.
            Contact.objects.create(
                **form.cleaned_data
            )                                   # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
            return redirect('/success')         # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form}                # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'contact.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.

def prices(request):
    return render(request, 'prices.html')

def ayuda(request):
    return render(request, 'ayuda.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# def contact_form(request):
#     errores = [] 
#     customer_name = request.POST['customer_name']
#     customer_email = request.POST['customer_email']
#     message = request.POST['message']
    
#     if len(customer_name) > 10:
#         errores.append('Largo del nombre mayor a 10 carácteres')

#     if not '@' in customer_email:
#         errores.append('Falta el arroba en el correo')

#     context = {'errores': errores}

#     if len(errores) > 0:
#         return render(request, 'welcome.html', context)
#     else:
#         return render(request, 'success.html', context)

def success(request):
    return render(request, 'success.html')

