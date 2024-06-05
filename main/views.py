from django.shortcuts import render
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
    return render(request, 'welcome.html')