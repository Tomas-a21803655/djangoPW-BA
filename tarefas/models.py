from django.db import models


# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]


class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=254, default='', blank=False)
    phone = models.IntegerField(blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=200, blank=False, default='')
    message = models.TextField(max_length=400, blank=False, default='')

    def __str__(self):
        return self.name[:50]
