from django.contrib import admin
from pessoa.models import Pessoa, Telefone

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Telefone)