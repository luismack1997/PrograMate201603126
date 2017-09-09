import math
elNumero=0
numero=1
temporal=0
contador1=[0]*10
contador2=[0]*10

def digitosiguales(tem):
    iguales=1
    temporal2=temporal
    temporal3=tem

    for x in range(0,int(math.log10(temporal))+1):
        contador1[temporal2 % 10]+=1
        temporal2=(temporal2-(temporal2 %10))/10
        contador2[temporal3 %10]+=1
        temporal3=(temporal3-(temporal3 %10))/10

    for x in range(0,10):
        if(contador1[x]!=contador2[x]):
            iguales=0

    for x in range(0,10):
        contador1[x]=0
        contador2[x]=0

    return iguales



while (elNumero==0):
    if(int(math.log10(numero))==int(math.log10(2*numero)) and int(math.log10(numero))==int(math.log10(3*numero)) and int(math.log10(numero))==int(math.log10(4*numero)) and int(math.log10(numero))==int(math.log10(5*numero)) and int(math.log10(numero))==int(math.log10(6*numero)) ):
        for y in range(2,7):
            temporal=numero
            a=digitosiguales(y*numero)
            if(a==0):
                elNumero=0
                numero+=1
                break
            else:
                elNumero=numero

    else:
        numero+=1

print elNumero
