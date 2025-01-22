from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    professor = {"name":"Roger","surname":"Sobrino","surname2":"Sobrino","mail":"rogersobrino@itic.com","role":"tutor","moduls":"M6"}
    template = loader.get_template('index_centre.html')
    dades = template.render({'nombre':professor["name"], 'cognom':professor["surname"],'cognom2':professor["surname2"],'correo':professor["mail"],'rol':professor["role"],'modulos':professor["moduls"]})
    return HttpResponse(dades)