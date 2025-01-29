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
        {"id": 1, "name": "Hugo", "surname": "Sansegundo", "surname2": "Costantini", "mail": "2023_hugo.sansegundo@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08, Big Data"},
        {"id": 2, "name": "Adrián", "surname": "Navarro", "surname2": "Pérez", "mail": "2023_adrian.navarro@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 3, "name": "Xavi", "surname": "Porras", "surname2": "del Pino", "mail": "2023_xavier.porras@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 4, "name": "Javier", "surname": "Giménez", "surname2": "Sánchez", "mail": "2023_javier.gimenez@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 5, "name": "Milena", "surname": "Vardumyan", "surname2": "Aleksanyan", "mail": "2023_milena.vardumyan@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M013, Big Data"},
        {"id": 6, "name": "Daniel", "surname": "Vallespin", "surname2": "Mellado", "mail": "2023_daniel.vallespin@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 7, "name": "Félix Bequet", "surname": "Balbin", "surname2": "Silva", "mail": "2023_felix.balbin@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 8, "name": "Victor Andrés", "surname": "Fernández", "surname2": "Álvarez", "mail": "2023_victor.fernandez@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08, IA"},
        {"id": 9, "name": "Lila", "surname": "Díez", "surname2": "Zhou", "mail": "2023_lila.diez@iticbcn.cat", "curs": "DAW2A", "moduls": "M06,M07,M08, ML"},
        {"id": 10, "name": "Arman", "surname": "Mohammed", "surname2": "Akther", "mail": "2023_arman.mohammed@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07, M08"},
        {"id": 11, "name": "Albert", "surname": "Penadés", "surname2": "Casajús", "mail": "2023_albert.penades@iticbcn.cat", "curs": "DAW2A", "moduls": "M06,M07,M08, ML"},
        {"id": 12, "name": "Natalia", "surname": "Casanellas", "surname2": "Blanquer", "mail": "2023_natalia.casanellas@iticbcn.cat", "curs": "DAW2A", "moduls": "M06, M07"}
    ]
    return render(request, 'alumnat.html', {"students": students})