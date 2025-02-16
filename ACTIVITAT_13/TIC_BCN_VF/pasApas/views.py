from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Usuari

# Create your views here.
def user_form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, 'form.html', context)

def login_sense_sessio(request):
    error = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuari = Usuari.objects.get(email=email)
            if password == usuari.contrasenya:  
                return render(request, 'index.html')
            else:
                error = "Credencials incorrectes."
        except Usuari.DoesNotExist:
            error = "Usuari no trobat."

    return render(request, 'login.html', {'error': error})


def login_amb_sessio(request):
    error = None
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            usuari = Usuari.objects.get(email=email, contrasenya=password)
            request.session['usuari_id'] = usuari.id 
            return redirect('inici')  
        except Usuari.DoesNotExist:
            error = "Credencials incorrectes."

    return render(request, 'login.html', {'error': error})

def inici(request):
    usuari_id = request.session.get('usuari_id') 

    if usuari_id:
        from .models import Usuari
        usuari = Usuari.objects.get(id=usuari_id)
        return render(request, 'inici.html', {'nom': usuari.nom})
    else:
        return redirect('login_sense_sessio')

def logout_view(request):
    request.session.flush()  
    return redirect('login_sense_sessio')