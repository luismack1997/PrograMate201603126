suma=1

for x in range(3,1002,2):
    for y in range(0,4):
            suma+=x**2-y*(x-1)

print suma
