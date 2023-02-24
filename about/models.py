from django.db import models

# Create your models here.
# Modelo para Formación = Course
class Course (models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    degree_title = models.CharField(max_length=300, verbose_name='Titulo Obtenido')
    description = models.TextField(verbose_name='Descripcion')
    link = models.URLField(max_length=180, blank=True, null=True, verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    # Pasos para convertir en español la aplicación en el admin y ordenacion de los registros
    # de acuerdo al campo 'created' de forma descendente (osea el ultimo proyecto agregado es el primero en mostrar)
    class Meta: 
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ['-created'] 

    # Cone esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su titulo
    def __str__(self): 
        return self.title


# Modelo para Conocimientos = Skills 
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name='Titulo')
    image = models.ImageField(upload_to='skills', verbose_name='Imagen')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    # Pasos para convertir en español la aplicación en el admin y ordenacion de los registros
    # de acuerdo al campo 'created' de forma descendente (osea el ultimo proyecto agregado es el primero en mostrar)
    class Meta: 
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['created'] 

    # Cone esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su titulo
    def __str__(self): 
        return self.title
