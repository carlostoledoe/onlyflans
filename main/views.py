from django.shortcuts import render
from django.http import HttpResponse
from main.pasteles import pasteles

# Create your views here.
def index(request):
    context = {'productos': pasteles}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def welcome(request):
    return render(request, 'welcome.html')