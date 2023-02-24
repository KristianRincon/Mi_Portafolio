from django.contrib import admin
from .models import Project

# Register your models here.
# Necesario para poder ver los campos ocultos 'created' y 'updated'
class ProjectAdmin(admin.ModelAdmin):
     # configuración extendida para cambiar ell nombre de la aplicación en el sector administrativo
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)