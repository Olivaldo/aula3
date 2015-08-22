from django.conf.urls import include, url, patterns

urlpatterns = patterns('pessoa.views',
    url(r'^$', 'index'),
    url(r'^excluir/(?P<codigo>\d+)/$', 'excluir', name='excluirPessoa'),
    url(r'^editar/(?P<codigo>\d+)/$', 'inserir', name='editarPessoa'),
    url(r'^pesquisar/$', 'pesquisar', name='pesquisarPessoa'),
    url(r'^form/inserir/$', 'inserirForm', name='inserirForm'),
)
