from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Noticia(models.Model):
    fecha_publicacion = models.DateTimeField()
    enlace = models.CharField(max_length=300)
    autor = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    titulo = models.TextField()
    resumen = models.TextField()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.fecha_publicacion.strftime('%Y-%m-%d')} - {self.titulo} - {self.autor}"


class Comentario(models.Model):
    texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.fecha_publicacion.strftime('%Y-%m-%d')} - {self.autor.username}"