import math
sumatotal=0
"""Solo hay que hacer el conteo combinatórico, una posición es perdedora cuando es de la froma 10101010001 i.e. cuando no hay dos 1's seguidos
el resto es simplemente hacer el conteo, sumamos 1 porque 2^30 es 1 seguido de 30 ceros lo cual es posición perdedora""" 
for x in range(0,30):
    if x%2==0:
        for y in range(0,x/2+1):
            sumatotal+=math.factorial(x-y)/(math.factorial(y)*math.factorial(x-2*y))
    else:
        for y in range(0,(x-1)/2+1):
            sumatotal+=math.factorial(x-y)/(math.factorial(y)*math.factorial(x-2*y))
print sumatotal+1