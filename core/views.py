# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect   
from pessoa.models import Pessoa 
from pessoa.forms import PessoaFormulario   

# Create your views here.
x = 1
def index(request):
    pessoas = Pessoa.objects.all()
    
    form = PessoaFormulario()

    return render(request, 'index.html', {'msg': u'That is it', 
    	                                  'pessoas':pessoas, 
    	                                  'form':form})
