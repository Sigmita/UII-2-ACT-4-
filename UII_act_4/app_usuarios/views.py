# app_usuarios/views.py
from django.shortcuts import render

def index(request):
    usuarios = [
        {"nombre": "Sofía López", "email": "sofia.l@netflix.com", "telefono": "555-2001"},
        {"nombre": "Ricardo Gómez", "email": "ricardo.g@netflix.com", "telefono": "555-2002"},
        {"nombre": "Valeria Castro", "email": "valeria.c@netflix.com", "telefono": "555-2003"},
    ]
    contexto = {'usuarios': usuarios}
    return render(request, 'index.html', contexto)