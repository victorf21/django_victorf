from django.shortcuts import render
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
