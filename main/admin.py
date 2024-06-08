from django.contrib import admin
from main.models import Flan, Contact
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, PersonaAdmin)

admin.site.register(Flan)