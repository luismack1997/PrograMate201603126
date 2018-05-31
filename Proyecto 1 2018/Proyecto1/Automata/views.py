# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import subprocess
from django.shortcuts import render
from django.views.generic import TemplateView
from collections import defaultdict
import os
ubicacionlatex='automata.tex'

# Convertidor---------------------------------------------------------------------------------------------------------------------------------------------------SS
Caracteres_Especiales={'+','?','*', '|','.'} 
Parentesis={'(',')'}

Problematicos={'+', '?', '*', '|'}
Unarios={'+', '?', '*'}
temporal=''
newtexto=''
error=0
numeroEstados=0
symbolos=[]
estados_aceptacion=[]
noEstadosAc=0
fThompson=[]
Estados=[]
estadoInicial=0
funcionfinal=[] 
def normales(caracter):
    global temporal
    global newtexto
    global error
    if caracter not in Caracteres_Especiales: 
        if temporal=='':
            newtexto=newtexto+caracter
            temporal='.'
        else: 
            newtexto=newtexto+caracter+'.'
            temporal='.'
    elif caracter in Unarios:
        if temporal in Problematicos:
            error=1
        elif temporal=='.':
            if newtexto[-1]=='.': 
                newtexto=newtexto[:-1]
                newtexto=newtexto+caracter+'.'
                temporal=caracter
            else: 
                newtexto=newtexto+caracter

def convertidor(texto):
    global temporal
    global newtexto
    temporal2=0
    temporal=""
    ora=0
    newtexto=''
    contador_parentesis_iz=0
    agregador=0
    for caracter in texto:
        if temporal2>0:
            if agregador>0:
                if newtexto[-1]=='.': 
                    newtexto=newtexto[:-1]
                    if caracter in Unarios:
                        newtexto=newtexto+'|'+caracter
                    else: 
                        newtexto=newtexto+'|'+caracter+'.'
                    agregador-=1
                    temporal2-=1
                else: 
                    if caracter in Unarios:
                        newtexto=newtexto+'|'+caracter
                    else: 
                        newtexto=newtexto+'|'+caracter+'.'
                    agregador-=1
                    temporal2-=1
            elif caracter in Unarios: 
                    newtexto=newtexto+caracter
                    temporal2-=1
                    temporal=''
            else: 
                    newtexto=newtexto+caracter+"."
                    temporal=''
                    temporal2-=1
        elif caracter=='|':
            if contador_parentesis_iz>0:
                agregador+=1
            elif ora==0:
                temporal=''
                ora=1
            else: 
                temporal=''
                newtexto=newtexto+'|'
        elif caracter=='(': 
            temporal=''
            contador_parentesis_iz+=1
        elif caracter==')':
            temporal='.'
            contador_parentesis_iz-=1
            temporal2+=1
        else:
            normales(caracter)
    if ora==1:
        newtexto=newtexto +'|'
    if texto[1] in Caracteres_Especiales:
        error=1
    elif contador_parentesis_iz!=0: 
        error=1
    if temporal2>0:
            if agregador>0:
                if newtexto[-1]=='.': 
                    newtexto=newtexto[:-1]
                    newtexto=newtexto+'|'
                    agregador-=1
                    temporal2-=1
                else: 
                    newtexto=newtexto+'|'
                    agregador-=1
                    temporal2-=1
    return newtexto
    

# Convetidor--------------------------------------------------------------------------------------------------------------------------------------------------------

#thompson AFD
def ThompsonExp(texto):
    ftThom={}    
    estadoinicial=0
    estadofinal=0
    estadoinicial2=0
    estadofinal2=0
    estadoinicial3=0
    estadoinicial3=0
    noEstados=0   
    operador1=0
    noEstadosNeg=0
    ftThom = defaultdict(dict)
    for caracter in texto:
        if caracter not in Caracteres_Especiales:
            noEstados+=2
            a=noEstados-2
            b=noEstados-1
            ftThom[a]={caracter:b}
            if operador1==0:
                estadoinicial=a
                estadofinal=b
                operador1=1
            elif operador1==1:
                estadoinicial2=a
                estadofinal2=b
                operador1=2
            elif operador1==2:
                estadoinicial3=a
                estadofinal3=b
                operador1=3
        elif caracter=='.':
            if operador1==2:
                ftThom[estadofinal].update(ftThom[estadoinicial2])
                estadofinal=estadofinal2
                operador1=1
                del ftThom[estadoinicial2]
            elif operador1==3:
                ftThom[estadofinal2]=ftThom[estadoinicial3]
                estadofinal2=estadofinal3
                operador1=2
                del ftThom[estadoinicial3]


        elif caracter=='|':
            noEstadosNeg-=1
            ftThom[noEstadosNeg].update({'ep':estadoinicial})
            ftThom[noEstadosNeg].update({'ep1':estadoinicial2})
            estadoinicial=noEstadosNeg
            ftThom[estadofinal].update({'ep':noEstados})
            ftThom[estadofinal2].update({'ep':noEstados})
            estadofinal=noEstados
            noEstados+=1
            operador1=1

        elif caracter=='+':
            if operador1==1:
                try: 
                    ftThom[estadofinal].update({'ep':estadoinicial})
                except:
                    ftThom[estadofinal]={'ep':estadoinicial}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial}
                estadoinicial=noEstadosNeg
                ftThom[estadofinal].update({'ep1':noEstados})
                estadofinal=noEstados
                noEstados+=1
            elif operador1==2:
                try: 
                    ftThom[estadofinal2].update({'ep':estadoinicial2})
                except:
                    ftThom[estadofinal2]={'ep':estadoinicial2}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial2}
                estadoinicial2=noEstadosNeg
                ftThom[estadofinal2].update({'ep1':noEstados})
                estadofinal2=noEstados
                noEstados+=1
            elif operador1==3:
                try: 
                    ftThom[estadofinal3].update({'ep':estadoinicial3})
                except:
                    ftThom[estadofinal3]={'ep':estadoinicial3}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial3}
                estadoinicial3=noEstadosNeg
                ftThom[estadofinal3].update({'ep1':noEstados})
                estadofinal3=noEstados
                noEstados+=1


        elif caracter=='?':
            if operador1==1:
                ftThom[estadoinicial].update({'ep':estadofinal})
            elif operador1==2:
                ftThom[estadoinicial2].update({'ep':estadofinal2})
            elif operador1==3:
                ftThom[estadoinicial3].update({'ep':estadofinal3})
        
        elif caracter=='*':
            if operador1==1:
                try: 
                    ftThom[estadofinal].update({'ep':estadoinicial})
                except:
                    ftThom[estadofinal]={'ep':estadoinicial}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial}
                estadoinicial=noEstadosNeg
                ftThom[estadofinal].update({'ep1':noEstados})
                estadofinal=noEstados
                noEstados+=1
                try: 
                    ftThom[estadoinicial].update({'ep1':estadofinal})
                except:
                    ftThom[estadoinicial]={'ep1':estadofinal}
            elif operador1==2:
                try: 
                    ftThom[estadofinal2].update({'ep':estadoinicial2})
                except:
                    ftThom[estadofinal2]={'ep':estadoinicial2}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial2}
                estadoinicial2=noEstadosNeg
                ftThom[estadofinal2].update({'ep1':noEstados})
                estadofinal2=noEstados
                noEstados+=1
                try: 
                    ftThom[estadoinicial2].update({'ep1':estadofinal2})
                except:
                    ftThom[estadoinicial2]={'ep1':estadofinal2}
            elif operador1==3:
                try: 
                    ftThom[estadofinal3].update({'ep':estadoinicial3})
                except:
                    ftThom[estadofinal3]={'ep':estadoinicial3}
                noEstadosNeg-=1
                ftThom[noEstadosNeg]={'ep':estadoinicial3}
                estadoinicial3=noEstadosNeg
                ftThom[estadofinal3].update({'ep1':noEstados})
                estadofinal3=noEstados
                noEstados+=1
                try: 
                    ftThom[estadoinicial3].update({'ep1':estadofinal3})
                except:
                    ftThom[estadoinicial3]={'ep1':estadofinal3}
    global numeroEstados
    global symbolos
    global estados_aceptacion
    global fThompson
    global Estados
    global noEstadosAc
    global estadoInicial
    estadoInicial=noEstadosNeg
    numeroEstados=0
    symbolos=[]
    estados_aceptacion=[]
    noEstadosAc=0
    fThompson=[]
    Estados=[]
    numero=noEstadosNeg
    while numero<=noEstados:
        if ftThom[numero]=={}:
            del ftThom[numero]
        else:
            for key in ftThom[numero].keys():
                if key=='ep' or key=='ep1':
                    transicion=(numero,'ep',ftThom[numero][key])
                    fThompson.append(transicion)
                    if 'ep' in symbolos:
                        pass 
                    else: 
                        symbolos.append('ep')
                else: 
                    transicion=(numero,key,ftThom[numero][key])
                    fThompson.append(transicion)
                    if key in symbolos:
                        pass 
                    else: 
                        symbolos.append(key)
            numeroEstados+=1
            Estados.append(numero)
        numero+=1
    numeroEstados+=1
    estados_aceptacion.append(noEstados-1)
    noEstadosAc=1
    Estados.append(noEstados-1)


class NFA:
    def __init__(self,numeroEstados,Estados,symbolos,noEstadosAc,estados_aceptacion,estadoInicial,fThompson):
        self.num_states = numeroEstados
        self.states = Estados
        self.symbols = symbolos
        self.num_accepting_states = noEstadosAc
        self.accepting_states = estados_aceptacion
        self.start_state = estadoInicial
        self.transition_functions = fThompson


class DFA:
    def __init__(self):
        self.num_states = 0
        self.symbols = []
        self.num_accepting_states = 0
        self.accepting_states = []
        self.start_state = 0
        self.transition_functions = []
        self.q = []
    def convert_from_nfa(self, nfa):
        self.symbols = nfa.symbols
        self.start_state = nfa.start_state

        nfa_transition_dict = {}
        dfa_transition_dict = {}
        
        # Combine NFA transitions
        for transition in nfa.transition_functions:
            starting_state = transition[0]
            transition_symbol = transition[1]
            ending_state = transition[2]
            
            if (starting_state, transition_symbol) in nfa_transition_dict:
                nfa_transition_dict[(starting_state, transition_symbol)].append(ending_state)
            else:
                nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]

        self.q.append((0,))
        
        # Convert NFA transitions to DFA transitions
        for dfa_state in self.q:
            for symbol in nfa.symbols:
                if len(dfa_state) == 1 and (dfa_state[0], symbol) in nfa_transition_dict:
                    dfa_transition_dict[(dfa_state, symbol)] = nfa_transition_dict[(dfa_state[0], symbol)]
                    
                    if tuple(dfa_transition_dict[(dfa_state, symbol)]) not in self.q:
                        self.q.append(tuple(dfa_transition_dict[(dfa_state, symbol)]))
                else:
                    destinations = []
                    final_destination = []
                    
                    for nfa_state in dfa_state:
                        if (nfa_state, symbol) in nfa_transition_dict and nfa_transition_dict[(nfa_state, symbol)] not in destinations:
                            destinations.append(nfa_transition_dict[(nfa_state, symbol)])
                    
                    if not destinations:
                        final_destination.append(None)
                    else:  
                        for destination in destinations:
                            for value in destination:
                                if value not in final_destination:
                                    final_destination.append(value)
                        
                    dfa_transition_dict[(dfa_state, symbol)] = final_destination
                        
                    if tuple(final_destination) not in self.q:
                        self.q.append(tuple(final_destination))

        # Convert NFA states to DFA states            
        for key in dfa_transition_dict:
            self.transition_functions.append((self.q.index(tuple(key[0])), key[1], self.q.index(tuple(dfa_transition_dict[key]))))
        
        for q_state in self.q:
            for nfa_accepting_state in nfa.accepting_states:
                if nfa_accepting_state in q_state:
                    self.accepting_states.append(self.q.index(q_state))
                    self.num_accepting_states += 1
    def print_dfa(self):
        global funcionfinal
        print(len(self.q))
        print("".join(self.symbols))
        print(str(self.num_accepting_states) + " " + " ".join(str(accepting_state) for accepting_state in self.accepting_states))
        print(self.start_state)
        funcionfinal=self.transition_functions
        
        for transition in sorted(self.transition_functions):
            print(" ".join(str(value) for value in transition))

def dibujador(): 
    global ubicacionlatex
    ubicacionlatex=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionlatex
    fichero = open(ubicacionlatex, 'w')
    fichero.write('\\documentclass[11pt,twoside]{article}')
    fichero.write("\n")
    fichero.write('\\usepackage{fancyhdr}')
    fichero.write('\n')
    fichero.write('\\usepackage{amsfonts, amsmath, amssymb}')
    fichero.write('\n')
    fichero.write('\\usepackage[none]{hyphenat}')
    fichero.write('\n')
    fichero.write('\\usepackage{dsfont}')
    fichero.write('\n')
    fichero.write('\\usepackage{tikz}')
    fichero.write('\n')
    fichero.write('\\usetikzlibrary{automata,positioning}')
    fichero.write('\n')
    fichero.write('\\pagestyle{fancy}')
    fichero.write('\n')
    fichero.write('\\fancyhf{}')
    fichero.write('\n')
    fichero.write('\\fancyfoot{}')
    fichero.write('\n')
    fichero.write('\\cfoot{\\thepage}')
    fichero.write('\n')
    fichero.write('\\lhead{MackTeck}')
    fichero.write('\n')
    fichero.write('\\rhead{\\today}')
    fichero.write('\n')      
    fichero.write("\\begin{document}")
    fichero.write('\n')
    fichero.write("\\begin{tikzpicture}[shorten >=1pt,node distance=2cm,on grid,auto] ")
    fichero.write('\n')
    numero=noEstadosNeg
    while numero<=noEstados:
        if numero in ftThom:  
            if s==0:
                fichero.write("\\node[state,initial] (q_0) {$q_0$};")
                fichero.write('\n')

                s+=1
            else:
                for x in salidos:
                    if numero in ftThom[x].values():
                        if len(ftThom[x])==1:
                            a='q_'+str(s)
                            b='q_'+str(guardador[salidos.index(x)])
                            a="\\node[state] ("+a+")[right=of "+b+"] {$"+a+"$};"  
                        elif d==0:
                            a='q_'+str(s)
                            b='q_'+str(guardador[salidos.index(x)])
                            a="\\node[state]("+a+") [above right=of "+b+"] {$"+a+"$};"  
                            d+=1 
                        else:
                            a='q_'+str(s)
                            b='q_'+str(guardador[salidos.index(x)])
                            a="\\node[state]("+a+") [below right=of "+b+"] {$"+a+"$};"  
                            d=0
                fichero.write(a)
                fichero.write('\n')
                salidos.append(numero)
                guardador.append(s)
                s+=1
        numero+=1   
    a='q_'+str(s)
    b='q_'+str(s-1)
    a="\\node[state,accepting]("+a+") [right=of "+b+"] {$"+a+"$};"  
    fichero.write(a)
    fichero.write('\n')
    salidos.append(s)  
    guardador.append(s)
    s=0
    numero=noEstadosNeg
    fichero.write("\\[path->]")
    fichero.write('\n')
    while numero<=noEstados:
        if numero in ftThom: 
            a='q_'+str(s)
            a='('+a+')'
            fichero.write(a) 
            for key in ftThom[numero].keys():
                a='q_'+str(s)
                a='('+a+')'
                b=ftThom[numero][key]
                b='q_'+str(b)
                if key=='ep' or key=='ep1':
                    es="\\epsilon"
                else:
                    es=key
                b="edge node {"+es+"} ("+b+")"
                fichero.write(b)
                fichero.write('\n')
        s+=1
        numero+=1

    fichero.write("\\end{tikzpicture}")
    fichero.write('\n')
    fichero.write('\\end{document}')
    fichero.close()
    cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & pdflatex automata.tex"
    subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read() 

ThompsonExp('ab|c.')
Automata=NFA(numeroEstados,Estados,symbolos,noEstadosAc,estados_aceptacion,estadoInicial,fThompson)
AutomataFinal=DFA()
AutomataFinal.convert_from_nfa(Automata)
AutomataFinal.print_dfa()
# Create your views here.

class IndexView(TemplateView):
    template_name='Automata/index.html'
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            screenname = request.POST.get("handle")  
            result=convertidor(screenname)
            ThompsonExp(result)
            global numeroEstados
            global symbolos
            global estados_aceptacion
            global fThompson
            global Estados
            global noEstadosAc
            global estadoInicial
            Automata=NFA(numeroEstados,Estados,symbolos,noEstadosAc,estados_aceptacion,estadoInicial,fThompson)
            AutomataFinal=DFA()
            AutomataFinal.convert_from_nfa(Automata)
        return render(request, 'Automata/index.html', {'result': result})



