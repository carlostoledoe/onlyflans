from django.shortcuts import render, redirect
from main.forms import ContactForm, RegisterForm
from main.models import Contact, Flan
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from main.data.api_mindicador import indicators


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
        'flanes': flanes_publicos,
        'indicators': indicators
        }
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
    if request.user.has_perm('main.delete_flan'):
        messages.warning(request, "Puedes borrar flanes")
        return render(request, 'prices.html')
    else:
        return render(request, 'prices.html')

def ayuda(request):
    return render(request, 'ayuda.html')

def register(request):
    form = RegisterForm()
    context = {'form': form}

    if request.method == 'GET':
        return render(request, 'registration/register.html', context)
    # En caso que sea post:
    form = RegisterForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        # Validación igualdad de password ingresado:
        if data['password'] != data['passRepeat']:
            messages.error(request, 'Ambas contraseñas deben ser iguales')
            return redirect('/accounts/register')
        # En caso que sean iguales, crea el usuario:
        User.objects.create_user(
            data['username'],
            data['email'],
            data['password']
        )
        messages.success(request, 'Usuario creado exitosamente!')
    # Si llega aquí, es porque se creó el usuario
    return redirect('/')

def success(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    messages.warning(request, "¡Has salido exitosamente!")
    return redirect('/')

class LoginViewPropia(SuccessMessageMixin ,LoginView):
    success_message = 'Bienvenido, '

# Esta vista solo la puede ver quien puede borrar flan
@permission_required('main.delete_flan')
def pruebas(request):
    return render(request, 'pruebas.html')

# Esta vista solo renderiza los tipos de suscripciones
def suscriptions(request):
    return render (request, 'registration/suscriptions.html')


def registerfree(request):
    return render(request, 'registration/registerfree.html')

def registerpremium(request):
    return render(request, 'registration/registerpremium.html')

def registerdiamond(request):
    return render(request, 'registration/registerdiamond.html')