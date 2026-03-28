from django.db import models
from django.contrib.auth.models import User


#Criando os modelos do projeto
class Assunto(models.Model):
    """Um assunto sobre o qual o usuario esta aprendendo"""
    assunto = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve uma representacao em string do modelo"""
        return self.assunto
    
class Aprendizado(models.Model):
    """Aprendizado especifico sobre um determinado assunto"""

    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    aprendizado = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'aprendizados'

    def __str__(self):
        """Devolve uma representacao de string do modelo"""

        if len(self.aprendizado) > 50:
            return self.aprendizado[:50] + '...'
        else:
            return self.aprendizado
