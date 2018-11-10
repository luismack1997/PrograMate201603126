encontrado=0
pandigital=1
a=""
y=1
guardador=0
nopandigital=0
while encontrado==0:
    if len(str(pandigital)+str(pandigital*2))>9:
        encontrado=1

    while len(a)<9:
        a=a+str(pandigital*y)
        y+=1
    
    if len(a)==9:
        for x in range(1,9):
            if str(x) not in a:
                nopandigital=1

    if nopandigital==0 and encontrado==0:
        guardador=int(a)
    nopandigital=0
    pandigital+=1
    y=1
    a=""

print guardador

