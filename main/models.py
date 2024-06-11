from django.db import models
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(
        max_length=64
    )
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    nombre = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=100)
    
    def __str__(self):
        name = self.nombre
        message = self.mensaje
        return f'{name} : {message}'