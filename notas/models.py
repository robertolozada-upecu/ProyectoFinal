from django.db import models

# Create your models here.
class Docente(models.Model):
    id= models.AutoField(primary_key=True)
    cedula= models.CharField(max_length=15, verbose_name="Cédula")
    apellidos= models.CharField(max_length=100, verbose_name="Apellidos")
    nombres= models.CharField(max_length=100, verbose_name="Nombres")
    correo= models.CharField(max_length=50, verbose_name="Correo electrónico")
    usuario= models.CharField(max_length=50, verbose_name="Usuario")
    tipo= models.IntegerField(verbose_name="Tipo")

    def __str__(self):
        fila= "Cédula: " + self.cedula + " - " + "Nombres: " + self.apellidos + " " + self.nombres
        return fila

class Estudiante(models.Model):
    id= models.AutoField(primary_key=True)
    cedula= models.CharField(max_length=15, verbose_name="Cédula")
    apellidos= models.CharField(max_length=100, verbose_name="Apellidos")
    nombres= models.CharField(max_length=100, verbose_name="Nombres")
    correo= models.CharField(max_length=50, verbose_name="Correo electrónico")
    usuario= models.CharField(max_length=50, verbose_name="Usuario")

    def __str__(self):
        fila= "Cédula: " + self.cedula + " - " + "Nombres: " + self.apellidos + " " + self.nombres
        return fila

