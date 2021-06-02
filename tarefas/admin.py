from django.contrib import admin

# Register your models here.
from .models import Tarefa, Contact, Comment, Networking, Quizz, QuizzAval, Comentarios

admin.site.register(Tarefa)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Networking)
admin.site.register(Quizz)
admin.site.register(QuizzAval)
admin.site.register(Comentarios)




