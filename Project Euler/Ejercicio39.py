import math
"""para resolver este problema hay que notar lo siguiente x+y+z=p, x^2+y^2=z^2 y al resolver tomando a p y a z constantes
llegamos a una cuadrática cuyo discriminante es z^2+2pz+p^2, por lo tanto existe terna si y solo si
dicho discriminante es positivo y la raíz de dicho discriminante es entero."""" 
soluciones=0
solucionmayor=0
numero=0
for p in range(3,1001): 
    for z in range(1,p-1):
        if z*z+2*z*p-p*p>0 and math.sqrt(z*z+2*z*p-p*p).is_integer():
            soluciones+=1
    if soluciones>solucionmayor:
        numero=p
        solucionmayor=soluciones
    soluciones=0
print numero