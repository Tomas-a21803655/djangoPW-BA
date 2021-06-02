from django.urls import path

from . import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('nova/', views.nova_tarefa_view, name='nova'),
    path('edita/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),
    # Buddy Abroad
    path('banner/', views.banner_page_view, name='banner'),
    path('aboutBA/', views.aboutBA_page_view, name='aboutBA'),
    path('team/', views.team_page_view, name='team'),
    path('tutorial/', views.tutorial_page_view, name='tutorial'),
    path('faq/', views.faq_page_view, name='faq'),
    path('contacts/', views.contacts_page_view, name='contacts'),
    path('aval/', views.aval_page_view, name='aval'),
    path('singlePageView/', views.singlePageView_page_view, name='singlePageView'),
    path('reviews/', views.reviews_page_view, name='reviews'),
    path('quizz/', views.quizz_page_view, name='quizz'),
    path('networking/', views.networking_page_view, name='networking'),
    path('networkingAddUser/', views.networkingAddUser_page_view, name='networkingAddUser'),
    path('quizzAval/', views.quizzAval_page_view, name='quizzAval'),
    path('quizzAvalResults/<int:quizzAval_id>', views.quizzAvalResults_page_view, name='quizzAvalResults'),
    path('comentarios/', views.comentarios_page_view, name='comentarios'),

]
