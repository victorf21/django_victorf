from django.shortcuts import render, redirect
# Create your views here.
def guardar_sesion(request):
    request.session['usuario'] = 'Juan'
    return render(request,'guardar_sesion.html')

def recuperar_sesion(request):
    usuario = request.session.get('usuario', 'Invitado')
    return render(request,'recuperar_sesion.html', {'usuario': usuario})

def eliminar_sesion(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    return redirect('recuperar_sesion')