from django.contrib import admin

from .models import Assunto, Aprendizado

modelos = [Assunto, Aprendizado]
admin.site.register(modelos)