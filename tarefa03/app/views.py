from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def usuarios(request):
    lista_usuarios = [
        {"nome": "Ana Júlia", "matrícula": 202401, "idade": 17, "cidade": "Riachuelo"},
        {"nome": "Burno Rafael", "matrícula": 202402, "idade": 18, "cidade": "São Tomé"},
        {"nome": "Danielly Rodrigues", "matrícula": 202403, "idade": 17, "cidade": "Barcelona"},
        {"nome": "Hemerson Daniel", "matrícula": 202404, "idade": 18, "cidade": "Barcelona"},
        {"nome": "Laíza Beatriz", "matrícula": 202405, "idade": 17, "cidade": "São Pedro"},
    ]

    context = {
        "usuarios" : lista_usuarios
    }
    return render(request, "usuarios.html", context)