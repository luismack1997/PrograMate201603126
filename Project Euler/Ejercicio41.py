import math

numero=87654321
elNumero=0
temporal=0
contador=[0]*10
pandigital=1
primo=1

while(elNumero==0):
    temporal=numero
    for x in range(1,int(math.log10(numero))+2):
        contador[temporal % 10]+=1
        temporal=(temporal-(temporal %10))/10

    for x in range(1,int(math.log10(numero))+2):
        if(contador[x]!=1):
            pandigital=0
            primo=0

    if(pandigital==1):
        for x in range(2,int(math.sqrt(numero))):
            if(numero % x==0):
                primo=0

    if(primo==1):
        elNumero=numero

    for x in range(0,9):
        contador[x]=0

    primo=1
    pandigital=1
    numero-=1

print elNumero
