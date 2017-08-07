#-*- coding:utf-8 -*-
primo=[None]*10001
primo.insert(1,2)
contador=1
numero=3

while(contador<10002):
    for x in range(0,contador,1):
        if numero % primo[x+1]==0:
            numero+=1
            break
        elif x==contador-1:
            primo.insert(contador+1,numero)
            numero+=1
            contador+=1
            break

print primo[10001]
