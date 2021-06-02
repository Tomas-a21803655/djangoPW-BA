from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Tarefa, Comment, Networking, QuizzAval
from .forms import TarefaForm, ContactForm, CommentForm, QuizzForm, NetworkingForm, QuizzAvalForm


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

    context = {'form': form, }

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


def quizzAval_page_view(request):
    form = QuizzAvalForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        messages.success(request, 'Quizz Completo!')
        return HttpResponseRedirect(reverse('tarefas:quizzAvalResults', args=(task.id,)))

    context = {'form': form, }

    return render(request, 'tarefas/quizzAval.html', context)


def quizzAvalResults_page_view(request, quizzAval_id):
    quizzAnswer = QuizzAval.objects.get(id=quizzAval_id)
    questionsAndAnswer = {
        "Qual é o layout utilizado neste website?(1pt)": "column",
        "Quantas aplicações compõem o Buddy Abroad?(1pt)": "tantoFaz",
        "O Buddy Abroad está disponível em iOS e Android?(1pt": 2,
        "O Buddy Abroad cobra quanto % de taxa?(1pt)": 30,
        "Posso ser um guia Buddy Abroad se conhecer bem a minha cidade?(1pt)": "True",
        "Quantos alunos trabalharam no Buddy Abroad?(1pt)": 2,
        "Quantas animações existem neste projecto?(1pt)": 2,
        "Existe algum output de audio neste website?(1pt)": "True",
        "Em que disciplina começou o projecto Buddy Abroad?(1pt)": "trabalho final de curso",
        "Acha que foi difícil desenvolver este projecto? (estimativa)(1pt)": "menor que 12",
    }

    correctThick = [
        [str(quizzAnswer.layout), True if quizzAnswer.layout == 'column' else False],
        [str(quizzAnswer.beAguide), True],
        [str(quizzAnswer.numberOfApps), True if quizzAnswer.numberOfApps == 2 else False],
        [str(quizzAnswer.percentageOfPay), True if quizzAnswer.percentageOfPay == 30 else False],
        [str(quizzAnswer.availablePlataforms), True if quizzAnswer.availablePlataforms == True else False],
        [str(quizzAnswer.howManyDevs), True if quizzAnswer.howManyDevs == 2 else False],
        [str(quizzAnswer.animations), True if quizzAnswer.animations == 2 else False],
        [str(quizzAnswer.audioQuestion), True if quizzAnswer.audioQuestion == True else False],
        [str(quizzAnswer.disciplina), True if quizzAnswer.disciplina == 'trabalho final de curso' else False],
        [str(quizzAnswer.diff), True if quizzAnswer.diff <= 12 else False],
    ]


    CorrectNumber = sum(x.count(True) for x in correctThick)

    context = {'correctNumber': CorrectNumber,
               'questionsAndAnswer': questionsAndAnswer, 'correctThick': correctThick}

    return render(request, 'tarefas/quizzAvalResults.html', context)
