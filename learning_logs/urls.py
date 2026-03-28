from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('assuntos/', views.assuntos, name='assuntos'),
    path('assunto/<int:assunto_id>/', views.assunto, name='assunto'),
    path('novo_assunto/', views.novo_assunto, name='novo_assunto'),
    path('novo_aprendizado/<int:assunto_id>', views.novo_aprendizado, name='novo_aprendizado'),
    path('editar_aprendizado/<int:aprendizado_id>', views.editar_aprendizado, name='editar_aprendizado')
]