import sympy
sumatemporal=0
primomayor=0
consecutivos=0
pasos=0
ab=0
for x in range(1,1001): 
    if sympy.isprime(x):
        for y in range(-1000, 1001):
            while consecutivos==0:
                if sympy.isprime(pasos*pasos+y*pasos+x):
                    pasos+=1
                    sumatemporal+=1
                    if sumatemporal>primomayor:
                        primomayor=sumatemporal
                        ab=y*x
                else:
                    consecutivos=1
            consecutivos=0
            sumatemporal=0
            pasos=0

print ab

