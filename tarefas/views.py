from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Tarefa, Comment
from .forms import TarefaForm, ContactForm, CommentForm


# Create your views here.


def home_page_view(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'tarefas/home.html', context)


def nova_tarefa_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:home'))

    context = {'form': form}

    return render(request, 'tarefas/nova.html', context)


def edita_tarefa_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:home'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'tarefas/edita.html', context)


def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))


# Buddy Abroad

def banner_page_view(request):
    return render(request, 'tarefas/banner.html')


def aboutBA_page_view(request):
    return render(request, 'tarefas/aboutBA.html')


def team_page_view(request):
    return render(request, 'tarefas/team.html')


def tutorial_page_view(request):
    return render(request, 'tarefas/tutorial.html')


def faq_page_view(request):
    return render(request, 'tarefas/faq.html')


def contacts_page_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Message Sent!')
        return HttpResponseRedirect(reverse('tarefas:contacts'))

    context = {'form': form}

    return render(request, 'tarefas/contacts.html', context)


def aval_page_view(request):
    return render(request, 'tarefas/aval.html')


def singlePageView_page_view(request):
    return render(request, 'tarefas/singlePageView.html')


def reviews_page_view(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:reviews'))

    average = list(Comment.objects.aggregate(Avg('rating')).values())[0] or 0

    context = {'form': form, 'comments': Comment.objects.all(), 'averageStars': round(average, 1)}

    return render(request, 'tarefas/reviews.html', context)
