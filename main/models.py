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

class Contact(models.Model):
    nombre = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    mensaje = models.CharField(max_length=100)