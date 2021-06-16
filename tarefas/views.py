from django.contrib import messages
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ContactForm, CommentForm, QuizzForm, NetworkingForm, QuizzAvalForm, ComentariosForm
from .models import Comment, Networking, QuizzAval


# Buddy Abroad Web
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
        return HttpResponseRedirect(reverse('users:index'))

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


def comentarios_page_view(request):
    form = ComentariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Formulário Completo!')
        return HttpResponseRedirect(reverse('tarefas:comentarios'))

    context = {'form': form, }

    return render(request, 'tarefas/comentarios.html', context)


def networkingEditUser_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networkingEditUser.html', context)


def networkingRemoveUser_page_view(request):
    context = {'usersGuide': Networking.objects.all().filter(typeOfUser=True),
               'usersTourist': Networking.objects.all().filter(typeOfUser=False)}

    return render(request, 'tarefas/networkingRemoveUser.html', context)


def deleteConfirmation_page_view(request, card_id):
    context = {'cardId': card_id}

    return render(request, 'tarefas/deleteConfirmation.html', context)


def apaga_card_view(request, card_id):
    Networking.objects.get(id=card_id).delete()
    return HttpResponseRedirect(reverse('tarefas:networkingRemoveUser'))


def editUserCard_view(request, card_id):
    card = Networking.objects.get(id=card_id)
    form = NetworkingForm(request.POST or None, instance=card)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('tarefas:networkingEditUser'))

    context = {'form': form, 'card_id': card_id}
    return render(request, 'tarefas/editUserCard.html', context)


def index_page_view(request):
    # Review Section get average and 3 reviews
    average = list(Comment.objects.aggregate(Avg('rating')).values())[0] or 0

    context = {'comments': Comment.objects.all()[:3], 'averageStars': round(average, 1),
               'reviewCount': Comment.objects.count(),
               }

    return render(request, 'tarefas/index.html', context)


def avalPt2_page_view(request):
    return render(request, 'tarefas/avalPt2.html')
