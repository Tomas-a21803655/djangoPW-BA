from django.contrib import admin

# Register your models here.
from .models import Tarefa, Contact, Comment, Networking

admin.site.register(Tarefa)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Networking)


