# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa, Telefone
from pessoa.forms import PessoaFormulario
from django.utils.translation import ugettext_lazy as _
#API
from pessoa.api import PessoaApi
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser

class Filtro_Pessoa(filtro.FilterSet):
    nome = filtro.AllLookupsFilter(name='nome')
    class Meta:
        model = Pessoa
        fields = ['idade','nome', 'ano']

class Api_Automatica(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaApi
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('nome')
    filter_class = Filtro_Pessoa
    permission_classes = (IsAdminUser,)
    paginate_by = 3

@api_view(['POST', 'GET'])

def api_manual(request):
    if request.method == 'POST':
        if request.POST.get('id', None):
            pessoa = Pessoa.objects.get(pk=request.POST['id'])
        else:
            pessoa = Pessoa()
        
        pessoaApi = PessoaApi(pessoa, data=request.data, partial=True)
        
        if pessoaApi.is_valid():
            pessoaApi.save()
            return Response(pessoaApi.data, status=status.HTTP_200_OK)
        else:            
            return Response(pessoaApi.data, status=status.HTTP_400_BAD_REQUEST) 
    if request.method == 'GET':        
        pessoas = Pessoa.objects.all()
        pessoaApi = PessoaApi(pessoas, many=True)
        return Response(pessoaApi.data)           



# Create your views here.
def index(request):
    pessoas = Pessoa.objects.all()
    msg = _(u"Isso é uma vergonha.")
    return render(request, 'conteudo.html', {'msg':msg, 'pessoas':pessoas})

def inserir(request, codigo=0): 
    if request.method == 'POST':                                    
        pessoa = Pessoa(                    
        id=request.POST.get('id') if request.POST.get('id', None) else None,
        nome=request.POST.get('nome'),
        idade=request.POST.get('idade'),
        ano=2015)        
        pessoa.save()    
        return HttpResponseRedirect('/')
    else:
        print 789
        pessoa = Pessoa.objects.get(pk=codigo)
        return render(request, 'index.html', {'msg':'Resultado da Busca', 'pessoa':pessoa})

def inserirForm(request):
    if request.method == 'POST':        
        form = PessoaFormulario(request.POST)

        if form.is_valid():
            form.save

    return render(request, 'index.html',{'form':form})         

def excluir(request, codigo):
    pessoa = Pessoa.objects.get(pk=codigo)
    pessoa.delete()
    return HttpResponseRedirect('/')

def pesquisar(request):      
    if request.method == 'GET':
        #selecao = {} #dicionário#        
        #if request.GET.get('buscar'):
        #    selecao['nome__contains'] = request.GET.get('buscar')
        
        #selecao['idade__gt'] = 12
        #pessoas = Pessoa.objects.filter(**selecao).order_by('nome')
        telefones = Telefone.objects.all() 
        #print Pessoa.objects.filter(telefone__telefone__icontains='5').count()      
        pessoas = Pessoa.objects.filter(nome__contains=request.GET.get('buscar')).order_by('nome') 
        #pessoas = Pessoa.objects.all()  
        print pessoas    
        
    return render(request, 'index.html', {'msg':'Resultado da Busca', 'pessoas':pessoas, 'telefones':telefones})