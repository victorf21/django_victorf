from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
def professors(request):
    professor = [{"name":"Roger","surname":"Sobrino","surname2":"G","mail":"rogersobrino@itic.com","curs":"DAW","role":"tutor","moduls":"M6, M7"},
                 {"name": "Josep", "surname": "Oriol", "surname2": "Roca", "mail": "joseporiol@gmail.com", "curs": "DAW", "role": "tutor", "moduls": "M6"}
                 
    ]
    return render(request,'index_centre.html',{'nombre':professor["name"], 'cognom':professor["surname"],'cognom2':professor["surname2"],'correo':professor["mail"],'curso':professor["curs"],'rol':professor["role"],'modulos':professor["moduls"]} )

def alumnat(request):
    students = [
        {"name": "Anna", "surname": "Martínez", "surname2": "López", "mail": "anna.martinez@itic.com", "curs": "DAW", "moduls": "M6, M8"},
        {"name": "Carles", "surname": "García", "surname2": "Pérez", "mail": "carles.garcia@itic.com", "curs": "DAM", "moduls": "M7, M9"}
    ]
    return render(request, 'alumnat.html', {"students": students})