from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def usuarios(request):

    lista_usuarios = [
        {
            'nome': 'Ana Júlia',
            'matricula': '2026001',
            'idade': 17,
            'cidade': 'Natal'
        },

        {
            'nome': 'Carlos',
            'matricula': '2026002',
            'idade': 18,
            'cidade': 'Mossoró'
        },

        {
            'nome': 'Maria',
            'matricula': '2026003',
            'idade': 16,
            'cidade': 'Parnamirim'
        },

        {
            'nome': 'João',
            'matricula': '2026004',
            'idade': 19,
            'cidade': 'Caicó'
        },

        {
            'nome': 'Fernanda',
            'matricula': '2026005',
            'idade': 17,
            'cidade': 'Currais Novos'
        },
    ]

    contexto = {
        'usuarios': lista_usuarios
    }

    return render(request, 'usuarios.html', contexto)