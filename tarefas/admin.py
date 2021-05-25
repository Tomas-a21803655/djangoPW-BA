from django.contrib import admin

# Register your models here.
from .models import Tarefa, Contact

admin.site.register(Tarefa)
admin.site.register(Contact)
