import sympy
encontrado=0
numero=""
permutable=0
x=1000
while encontrado==0:
    if sympy.isprime(x) and x!=1487: 
        y=1
        while (x+y)<=9999 and (x+2*y)<9999:
            if sympy.isprime(x+y) and sympy.isprime(x+2*y) and sorted(str(x))==sorted(str(x+y)) and sorted(str(x))==sorted(str(x+2*y)):
                encontrado=1
                numero=str(x)+str(x+y)+str(x+2*y)
                y=9999
            y+=1           
                
    x+=1

print numero

        