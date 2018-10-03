sumatotal=0
sumatemporal=0
for x in range(1,2000000):
    for char in str(x):
        sumatemporal+=int(char)**5
    if sumatemporal==x:
        sumatotal+=x
    sumatemporal=0
print sumatotal-1