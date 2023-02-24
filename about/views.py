from django.shortcuts import render
from .models import Course, Skill

# Create your views here.
def about(request):
    # enviamos al render todos los datos de la tabla render y todos los datos de la tabla skills
    Courses = Course.objects.all()
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'courses':Courses, 'skills':skills})
