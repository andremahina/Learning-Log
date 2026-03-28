from django import forms

from .models import Assunto, Aprendizado


class AssuntoForm(forms.ModelForm):
    """Formulario para adicao de novos assuntos do usuario"""
    class Meta:
        model = Assunto # Modelo que serve de base para o formulario
        fields = ['assunto']
        labels = {'assunto' : 'assunto'}

class AprendizadoForm(forms.ModelForm):
    """Formulario para adicao de novos aprendizados relativos a um assunto especificado"""
    class Meta:
        model = Aprendizado
        fields = ['aprendizado']
        labels = { 'Aprendizado' : 'Aprendizado' }
        widgets = {'aprendizado' : forms.Textarea(attrs={ 'cols' : 80 })}