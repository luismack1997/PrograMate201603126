import math
sumatotal=0
for x in range(1,10):
    y=1
    while len(str(int(math.pow(x,y))))<=y and y<50:
        if len(str(int(math.pow(x,y))))==y:
            sumatotal+=1
        y+=1

print sumatotal

