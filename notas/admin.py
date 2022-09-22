from django.contrib import admin
from .models import Docente
from .models import Estudiante

# Register your models here.
admin.site.register(Docente)
admin.site.register(Estudiante)