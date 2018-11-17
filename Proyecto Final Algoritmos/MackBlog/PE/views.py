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
    'Red',
    'Integer',
    'Yellow',
    'Menor',
    'Mayor'
)
t_Integer= r'[0-9]+?'
t_Purple= r'(if|for|else|while|return|import|elif)'
t_Blue=r'(and|not|global|[^a-z]in[^a-z]|def|file)'
t_Yellow=r'(range|print|class)'
t_Red=r'(int|str)'
t_Menor=r'<'
t_Mayor=r'>'
def t_error(t):
    t.lexer.skip(1)
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
            context+=str(contador) +". "+ '<font color="Green">'  +line+ "</font>"
        else:
            lexer.input(line)
            temporal=line
            for tok in lexer:
                if tok.type=='Menor':
                    a= ' &gt '
                    temporal=temporal.replace(tok.value, a)
                if tok.type=='Mayor':
                    a= ' &lt '
                    temporal=temporal.replace(tok.value, a)
            line=temporal
            lexer.input(line)
            temporal=line
            for tok in lexer:
                if tok.type=='Yellow':
                        a='<font color="Yellow">'+tok.value+"</font>"
                        temporal=temporal.replace(tok.value, a)
                if tok.type=='Blue':
                    a='<font color="Blue">'+tok.value+"</font>"
                    temporal=temporal.replace(tok.value, a)
            line=temporal
            lexer.input(line)
            temporal=line
            for tok in lexer:
                if tok.type=='Purple':
                    a='<font color="brown">'+tok.value+"</font>"
                    temporal=temporal.replace(tok.value, a)
                if tok.type=='Integer':
                    a='<font color="Orange">'+str(tok.value)+"</font>"
                    temporal=temporal.replace(tok.value, a)
                if tok.type=='Red':
                    a='<font color="Red">'+tok.value+"</font>"
                    temporal=temporal.replace(tok.value, a)
            context+=str(contador) +". "+ temporal
            contador+=1
    fichero.close()
    return render(request, 'PE/detail'+str(numero)+'.html', {'problema': problema, 'context':context})
