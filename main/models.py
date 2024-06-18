from django.db import models
import uuid
from django.contrib.auth.models import User

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
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=500)
    
    def __str__(self):
        name = self.nombre
        message = self.mensaje
        return f'{name} : {message}'

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('diamond', 'Diamond'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.user.username