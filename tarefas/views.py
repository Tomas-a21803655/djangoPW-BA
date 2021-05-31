from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Tarefa, Comment, Networking
from .forms import TarefaForm, ContactForm, CommentForm, QuizzForm, NetworkingForm


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

    starRatings0 = Comment.objects.filter(rating=1).count()
    starRatings1 = Comment.objects.filter(rating=2).count()
    starRatings2 = Comment.objects.filter(rating=3).count()
    starRatings3 = Comment.objects.filter(rating=4).count()
    starRatings4 = Comment.objects.filter(rating=5).count()

    context = {'form': form, 'comments': Comment.objects.all(), 'averageStars': round(average, 1),
               'starRatings0': starRatings0,
               'starRatings1': starRatings1,
               'starRatings2': starRatings2,
               'starRatings3': starRatings3,
               'starRatings4': starRatings4,
               'reviewCount': Comment.objects.count(),
               }

    return render(request, 'tarefas/reviews.html', context)


def quizz_page_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Quizz Completed!')
        return HttpResponseRedirect(reverse('tarefas:quizz'))

    context = {'form': form,}

    return render(request, 'tarefas/quizz.html', context)


def networking_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networking.html', context)


def networkingAddUser_page_view(request):
    form = NetworkingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:networking'))

    context = {'form': form}

    return render(request, 'tarefas/networkingAddUser.html', context)
