from django.shortcuts import render, redirect
from main.forms import ContactForm
import json
import os

# Create your views here.
def index(request):
    # file_path = 'main/data/pasteles.json'
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'pasteles.json') # Obtiene el directorio de views.py y combina con 'data' y 'personas.json' para crear la ruta. Esta forma es portable, mantenible y buena práctica
    with open(file_path, 'r') as file: 
        pasteles = json.load(file)
    context = {'productos': pasteles}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def welcome(request):
    if request.method == 'GET':
        form = ContactForm() # Se crea una instancia del formulario FlanForm sin datos iniciales.
        context = {'form': form} # Se crea un contexto que contiene el formulario vacío.
        return render(request, 'welcome.html', context) # Se renderiza la plantilla 'welcome.html' con el contexto.
    else:
        form = ContactForm(request.POST) # Se crea una instancia de FlanForm con los datos enviados en la solicitud POST.
        if form.is_valid(): # Se verifica si los datos del formulario son válidos.
            return redirect('/success') # Si el formulario es válido, se redirige al usuario a la URL '/success'.
        context = {'form': form} # Se crea un contexto que contiene el formulario con los datos (válidos o no).
        return render(request, 'welcome.html', context) # Se vuelve a renderizar la plantilla con el contexto actualizado.

def prices(request):
    return render(request, 'prices.html')

def ayuda(request):
    return render(request, 'ayuda.html')

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