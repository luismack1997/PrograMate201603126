
import math


F1=1
F2=1
ElFibonacci=1
contador=2
digitos=0

while (digitos<1000):
    digitos=0
    if ElFibonacci==1:
        F1=F1+F2
        digitos=math.log10(F1)+1
        ElFibonacci=0
        contador+=1
    else:
        F2=F1+F2
        digitos=math.log10(F2)+1
        ElFibonacci=1
        contador+=1


print contador
print F1
print F2
