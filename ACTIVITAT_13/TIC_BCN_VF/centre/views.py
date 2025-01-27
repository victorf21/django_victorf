from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
def professors(request):
    professors = [
        {"name": "Roger", "surname": "Sobrino", "surname2": "Gil", "mail": "rogersobrino@itic.com", "curs": "DAW", "role": "tutor", "moduls": "M7"},
        {"name": "Josep", "surname": "Oriol", "surname2": "Roca", "mail": "joseporiol@itic.com", "curs": "DAW", "role": "tutor", "moduls": "M6"},
        {"name": "Juanma", "surname": "Sanchez", "surname2": "Bel", "mail": "juanmasanchez@itic.com", "curs": "DAW", "role": "tutor", "moduls": "M6"}
    ]
    return render(request, 'professors.html', {"professors": professors})

# Vista para alumnat
def alumnat(request):
    students = [
        {"name": "Victor", "surname": "Fernández", "surname2": "Álvarez", "mail": "victorf@itic.com", "curs": "DAW", "moduls": "M6, M7, M8"},
        {"name": "Albert", "surname": "Penades", "surname2": "Casajus", "mail": "albert@itic.com", "curs": "DAW", "moduls": "M6, M7, M8"},
        {"name": "Victor", "surname": "Fernández", "surname2": "Álvarez", "mail": "victorf@itic.com", "curs": "DAW", "moduls": "M6, M7, M8"}
    ]
    return render(request, 'alumnat.html', {"students": students})