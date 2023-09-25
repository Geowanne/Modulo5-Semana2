from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm

def inicio(request):
    return render(request, "index.html")



def contato(request):
    sucesso = False

    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST) 

        if form.is_valid():
            sucesso = True

    contexto = {
        'telefone': '(42) 99937-1559',
        'responsavel': 'Geovane Joanico',
        'formulario': form,
        'sucesso': sucesso
    }


    return render(request, "contato.html", contexto)

def reserva(request):
    if request.method == 'GET':
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)

    contexto = {    
        'form': form    
    }


    return render(request, "reserva.html", contexto)        
