from django.shortcuts import render
from .models import Bebida

def index(request):
    bebidas = Bebida.objects.all()
    return render(request, 'index.html', {'bebidas': bebidas})