from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=100, blank=True)
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField(null=True, blank=True)
    editorial = models.CharField(max_length=200, blank=True)
    genero = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='resenas')
    autor = models.CharField(max_length=200)
    calificacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reseña de {self.libro.titulo} - {self.calificacion}★'
