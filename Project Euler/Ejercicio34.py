temporal=0
sumadigitos=0
sumanumeros=0
temporal=0

def factorial(n):
    temporal2=1
    for y in range(0,n):
        temporal2=temporal2*(y+1)
    return temporal2


for x in range(3,2177281):
    temporal=x
    while (temporal>0):
        sumadigitos+=factorial(temporal%10)
        temporal=(temporal-temporal%10)/10
    if(sumadigitos==x):
        print x
        sumanumeros+=x
    temporal=0
    sumadigitos=0

print sumanumeros
