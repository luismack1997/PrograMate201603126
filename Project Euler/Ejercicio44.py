import math
encontrado=0
x=2
while encontrado==0:
    pk=x*(3*x-1)
    for y in range(x-1,0,-1):
        pj=y*(3*y-1)
        if ( (1+math.sqrt( 1+12*(pk+pj) ) )/6 ).is_integer() and ( (1+math.sqrt( 1+12*(pk-pj) ) )/6 ).is_integer():
            encontrado=pk-pj
    x+=1


print encontrado/2