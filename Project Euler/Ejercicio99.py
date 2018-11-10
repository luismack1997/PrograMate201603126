import math
mayor=0
line=1
fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio99.txt','r')
archivo=fichero.readlines()
fichero.close()
mayorlinea=0

for elemento in archivo:
    a=int(elemento[:elemento.index(",")])
    b=int(elemento[elemento.index(",")+1:])
    c=b*math.log10(a)
    if c>mayor:
        mayor=c
        mayorlinea=line
    line+=1


print mayor
print mayorlinea


     