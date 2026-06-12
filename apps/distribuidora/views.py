from django.shortcuts import render
from .models import Bebida

def index(request):
    return render(request, 'index.html')