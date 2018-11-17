import sympy
encontrado=0
contador=1
lista=[]

while encontrado==0:
    p=sympy.prime(contador)
    for x in range(0,len(str(p))):
        lista.append(x)
    contador+=1