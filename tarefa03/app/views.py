from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    user_list = [
        {"nome": "Elayne", "matricula":"20231181110015", "idade": 17, "cidade":"Elói de Souza"},
        {"nome": "Juliana", "matricula":"20231181110019", "idade": 18, "cidade":"Boa Saúde"},
        {"nome": "Rebeca", "matricula":"20231181110016", "idade": 19, "cidade":"São Paulo"},
        {"nome": "Leticia", "matricula":"20231181110020", "idade": 16, "cidade":"Serra Caiada"},
        {"nome": "Carla", "matricula":"20231181110030", "idade": 15, "cidade":"Natal"},
    ]

    context = {
        "usuarios": user_list,
    }
    return  render(request, 'usuarios.html', context)