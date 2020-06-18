from django.db import models

# Create your models here.
class Califas(models.Model):
    materia=models.CharField(max_length=30)
    alumno=models.CharField(max_length=30)
    cal1=models.IntegerField()
    cal2=models.IntegerField()
    cal3=models.IntegerField()
