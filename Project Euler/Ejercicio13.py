fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio13.txt','r')
lista=[0]*102
suma=0
for x in range(1,101):
    lista[x]=fichero.readline()
    print lista[x]

for x in range(1,101):
    suma+=int(lista[x][:14])
print suma
