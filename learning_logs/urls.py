from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('assuntos/', views.assuntos, name='assuntos'),
    path('assunto/<int:assunto_id>/', views.assunto, name='assunto')
]