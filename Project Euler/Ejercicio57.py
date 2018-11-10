x=3
y=2
sumatotal=0
temporal1=0
temporal2=0
for z in range(1,1001):
    if len(str(x))>len(str(y)):
        sumatotal+=1
    temporal1=2*y+x
    temporal2=y+x
    x=temporal1
    y=temporal2

print sumatotal
    