from django.db import models

# Create your models here.
class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=50)
    cognom = models.CharField(max_length=50)
    contrasenya = models.CharField(max_length=100)