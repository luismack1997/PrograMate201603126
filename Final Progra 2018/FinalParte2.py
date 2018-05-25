# -*- coding: utf-8 -*-
#solución hecha por Luis E. Mack
#nuestra expresión regular es (0|1)*0

#primero basándonos en el dibujo del autómata definimos cada una de las partes del autómata (tf es función transición)
states = {1,2,3}
accept_states = {2}
alphabet = {0,1}
tf = {1:{'0':2,'1':3},
       2:{'0':2,'1':3},
       3:{'0':2,'1':3},
       }

start_states = 1
#ea=Estado Actual
#ac=Estado Aceptación
#al=Alfabeto
#ein=Estado Inicial
#ft=Función Transición
class DFA:
    ea=None
    def __init__(self,es,ac,al,ein,ft):
        self.es = es
        self.al = al
        self.ft = ft
        self.ein= ein
        self.ac = ac
        self.ea = ein
        self.aceptado=0
        return
#definimos nuestra función que cambia de estado
    def CambioEstado(self, caracter):
        try:
            self.ea =self.ft[self.ea][caracter]
        except:
            self.ea=None
#definimos nuestra función que envía al estado inicial (en caso que pasemos varias cadenas)
    def IrEstadoInicial(self):
        self.ea = self.ein
#finalmente defninimos nuestra función que acepta la cadena, primero enviamos al estado inicial, luego 
#hacemos la transición a través del caracter y por último verificamos si cayó o no en uno de aceptación
    def Aceptador(self, cadena):
        self.IrEstadoInicial()
        cadena=str(cadena)
        for caracter in cadena:
            self.CambioEstado(caracter)
            if self.ea in self.ac: 
                self.aceptado=1
            else: 
                self.aceptado=0
        return self.aceptado


Automata=DFA(states,accept_states,alphabet,start_states,tf)

#finalmente pongo varias cadenas para probar que el autómata funciona (1 si lo aceptó 0 si no lo hizo) 
a=Automata.Aceptador(101001)
a1=Automata.Aceptador(1001110100)
a2=Automata.Aceptador(110101011)
a3=Automata.Aceptador(1001110101010)
a4=Automata.Aceptador(101110100010)
a5=Automata.Aceptador(11001110101011)
a6=Automata.Aceptador(1011100101)
a7=Automata.Aceptador(10)
print a #imprimirá 0 pues no lo aceptó
print a1 #1 pues sí
print a2 #0
print a3 #1
print a4 #1
print a5 #0
print a6 #0
print a7 #1