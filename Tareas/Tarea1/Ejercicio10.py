#Este ejercicio no esta completo todavia
#-*- coding:utf-8 -*-
primo=[None]*200001
primo.insert(1,2)
contador=1
numero=3
sumaprimos=2

while(contador<200002):
    for x in range(0,contador,1):
        if numero % primo[x+1]==0:
            numero+=1
            break
        elif primo[x]>numero**(1/2):
            primo.insert(contador+1,numero)
            if numero<2000000:
                sumaprimos+=numero
                print sumaprimos
            numero+=1
            contador+=1
            break


print primo[200001]
