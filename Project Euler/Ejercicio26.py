sumalarga=1
sumatemporal=1
d=0
y=9
for x in range(1,1000):
    if x%2!=0 and x%5!=0:
        while y%x!=0:
            y=y*10+9
            sumatemporal+=1
        if sumatemporal>sumalarga:
            d=x
            sumalarga=sumatemporal
        sumatemporal=1
        y=9
print d


