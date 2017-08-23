fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio8.txt','r')
lista=[0]*2
lista[0]=fichero.read()
print lista[0]

x=0
productomayor=1
productotemporal=1
while (x<=987):
    for y in range(x,x+13):
        productotemporal*=int(lista[0][y:y+1])
    if(productotemporal>productomayor):
        productomayor=productotemporal
    x+=1
    productotemporal=1

print productomayor
