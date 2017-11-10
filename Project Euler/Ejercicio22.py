import os
ubicacionarchivo=os.path.dirname( os.path.realpath(__file__) )+"\\"+"Ejercicio22.txt"
fichero = open(ubicacionarchivo, 'r')
texto=fichero.read()
suma=0
posiciones=[pos for pos, char in enumerate(texto) if char == "\""]
Letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
temporal=[]
for x in range(1,len(posiciones)+1,2):
    temporal.append(texto[posiciones[x-1]+1:posiciones[x]])
temporal.sort()
for x in range(1,len(temporal)+1):
    palabras = [ch for ch in temporal[x-1]]
    sumatemporal=0
    for y in range(0,len(palabras)):
        sumatemporal+=Letras.index(palabras[y])+1
    suma+=sumatemporal*x

print suma
