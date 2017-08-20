import math


F1=1
F2=1
contador=2
cambio=0
Elfibonacci=1
n=input("Que fibonacci quiere saber?\n")


while (contador<n):
    if Elfibonacci==1:
        F1=F1+F2
        Elfibonacci=0
        contador+=1
        cambio=F1
    else:
        F2=F1+F2
        Elfibonacci=1
        contador+=1
        cambio=F2
        
if(n==1 or n==2):
    print 1
else:
    print cambio
