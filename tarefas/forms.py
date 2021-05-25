from django import forms
from django.forms import ModelForm
from .models import Tarefa, Contact


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. John'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Doe'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. johndoe@mail.com'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ex. 910000000'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex. Found a bug'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here'}),
        }
