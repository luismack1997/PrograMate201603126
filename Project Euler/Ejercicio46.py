import sympy
import math
encontrado=0
compuestos=9
noencontrado=1


noagregar=0

listaPrimos=[]
listaPrimos.append(2)

for x in range(3,100000):
    y=0
    while listaPrimos[y]<=int(math.sqrt(x)):
        if x%listaPrimos[y]==0:
            noagregar=1
        y+=1
    y=0
    if noagregar==0:
        listaPrimos.append(x)
    noagregar=0
print "he terminado de generar la lista"

while encontrado==0:
    if (compuestos in listaPrimos)==False:
        x=1
        y=0
        while 2*x*x<compuestos:
            if (2*x*x+listaPrimos[y])==compuestos:
                x=compuestos
                noencontrado=0
            elif (2*x*x+listaPrimos[y])>compuestos:
                x+=1
                y=0
            else:
                y+=1
        if noencontrado==1:
            encontrado=compuestos
        noencontrado=1
    compuestos+=2

print encontrado

