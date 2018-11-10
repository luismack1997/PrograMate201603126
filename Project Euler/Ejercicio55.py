LyrchelNumbers=0
iterations=0
for x in range(1,10000):
    temporal=x
    while iterations<50:
        a=""
        for character in str(temporal):
            a=character+a
        temporal=int(a)+temporal
        a=""
        for character in str(temporal):
            a=character+a
        if a==str(temporal):
            iterations=50
            LyrchelNumbers+=1
        else:
            iterations+=1
    iterations=0

print 9999-LyrchelNumbers

