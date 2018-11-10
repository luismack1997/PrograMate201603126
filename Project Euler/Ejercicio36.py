y=""
a=""
sumatotal=0
for x in range(1,1000001):
    for character in str(x):
        y=character+y
    if y==str(x):
        z=bin(x)[2:]
        for character in z:
            a=character+a
        if a==z:
            sumatotal+=x
    a=""
    y=""

print sumatotal