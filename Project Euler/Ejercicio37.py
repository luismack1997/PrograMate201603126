import sympy
contador=0
n=10
primo=0
sumatotal=0
while contador<11:
    if sympy.isprime(n):
        for x in range(1,len(str(n))):
            if sympy.isprime(int(str(n)[x:len(str(n))]))==False:
                primo=1
                break
            elif sympy.isprime(int(str(n)[:len(str(n))-x]))==False:
                primo=1
                break
        if primo==0:
            contador+=1
            sumatotal+=n
        primo=0
    n+=1

print sumatotal