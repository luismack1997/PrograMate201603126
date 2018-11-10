# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Problemas
import os
import sys  
import ply.lex as lex
tokens=(
    'Purple',
    'Blue',
    'Green',
    'Integer',
    'Yellow',
)
t_Integer= r'\d+'
t_Purple= r'(if|for|else|while|return|import|elif)'
t_Blue=r'(and|not|in|global|def|file)'
t_Yellow=r'(range|print)'
t_Green=r'(int|str)'

lexer=lex.lex()
reload(sys)  
sys.setdefaultencoding('utf8')
# Create your views here.

def index(request):
    all_problems = Problemas.objects.all()
    context= {
        'all_problems': all_problems
    }
    return render(request, 'PE/index.html', context)

def detail(request, numero):
    problema=get_object_or_404(Problemas, pk=numero)
    context=""
    fichero=file(os.path.dirname(os.path.realpath(__file__))+"/static/PE/Problema"+str(numero)+".text","r")
    contador=1
    for line in fichero:
        if line[0]=="#":
            context+=str(contador) +". "+ '<font color="rgb(0, 102, 0)">'  +line+ "</font>"
        else:
            lexer.input(line)
            while True:
                tok = lexer.token()
                if not tok: 
                    break      # No more input
                print(tok)
            context+=str(contador) +". "+ line
            contador+=1
    fichero.close()
    return render(request, 'PE/detail'+str(numero)+'.html', {'problema': problema, 'context':context})
