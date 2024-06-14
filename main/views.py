from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import Contact, Flan
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {'flanes': flanes_publicos}
    return render(request, 'index.html', context)

@login_required
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

def register(request):
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    messages.success(request, "¡Has salido exitosamente!")
    return redirect('/')
