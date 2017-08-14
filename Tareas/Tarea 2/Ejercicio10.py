#-*- coding:utf-8 -*-
#El ejercicio se tarda como 45min pero lo calcula bien
import math
primo=[None]*200004
primo.insert(1,2)
contador=1
numero=3
sumaprimos=2

while(contador<200000):
    for x in range(0,contador,1):
        if numero % primo[x+1]==0:
            numero+=1
            break
        elif primo[x+1]>math.sqrt(numero):
            primo.insert(contador+1,numero)
            if numero<2000000:
                sumaprimos+=numero
            numero+=1
            contador+=1
            break


print sumaprimos
