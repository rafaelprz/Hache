from django.db import models

# Create your models here.
class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    tipo = models.CharField(max_length=50)
    description = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_vinos') 


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Bebida"
        verbose_name_plural = "Bebidas"

