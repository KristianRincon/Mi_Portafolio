from django.contrib import admin
from .models import Course, Skill

# Registrar la aplicacione about en el sector administrativo
class AboutAdmin(admin.ModelAdmin):
     # configuración extendida para cambiar el nombre de la aplicación en el sector administrativo
    readonly_fields = ('created', 'updated')

admin.site.register([Course, Skill], AboutAdmin)
