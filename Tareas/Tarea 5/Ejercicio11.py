fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio11.txt','r')
lista=[0]*20

#with open("file.txt", "r") as ins:
#    array = []
#    for line in ins:
#        array.append(line)

x=0
productomayor=1
productotemporal=1


for x in range(0,20):
    lista[x]=fichero.readline()
    lista[x] = lista[x].replace(" ", "")
    print lista[x]

#mtodo de lineas arriba y abajo
for y in range(0,17):
    for x in range(0,20):
        for z in range(y,y+4):
            productotemporal*=int(lista[z][x:x+2])
        if(productotemporal>productomayor):
            productomayor=productotemporal
        productotemporal=1
    productotemporal=1

#mtodo diagonales hacia la izquierda
for y in range(0,17):
    for x in range(4,20):
        w=0
        for z in range(y,y+4):
                productotemporal*=int(lista[z][x-w+4:x-w+6])
                w+=2
                if(productotemporal>productomayor):
                    productomayor=productotemporal
        productotemporal=1
    productotemporal=1


#mtodo diagonales hacia la derecha
for y in range(0,17):
    for x in range(0,17):
        w=0
        for z in range(y,y+4):
                productotemporal*=int(lista[z][x+w:x+w+2])
                w+=2
                if(productotemporal>productomayor):
                    productomayor=productotemporal
        productotemporal=1
    productotemporal=1

#mtodo de derecha e izquierda
for y in range(0,20):
    for x in range(0,17):
        for z in range(0,4):
            productotemporal*=int(lista[y][x+2*z:x+2*z+2])
        if(productotemporal>productomayor):
            productomayor=productotemporal
        productotemporal=1
    productotemporal=1

print productomayor
