# coding: utf-8
from django.shortcuts import render

# Create your views here.
x = 1
def index(request):
    return render(request, 'index.html', {'msg': u'That is it'})
