from django.db import models

class Configuracion(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    nutrientes = models.FloatField()
    luz = models.BooleanField()

    def __str__(self):
        return f"Temperatura: {self.temperatura}°C,    Humedad: {self.humedad}%,    Nutrientes: {self.nutrientes} pH,    Luz: {'Encendida' if self.luz else 'Apagada'}"
