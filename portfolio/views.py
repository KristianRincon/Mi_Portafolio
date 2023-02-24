from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    # obtener los registros desde el archivo models y la clase Project (que son los archivos de la bd)
    projects = Project.objects.all()
    # Mediante el diccionario transferimos todos los registros al templete portafolio
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

