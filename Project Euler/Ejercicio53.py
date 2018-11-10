
encontrado=0
sumatotal=0

for n in range(23,101):
    a=1
    b=1
    r=1
    while encontrado==0:
        for y in range(n,n-r,-1):
            a=a*y
        for z in range(1,r+1):
            b=b*z
        if a/b>=1000000:
            encontrado=1
        else: 
            r+=1
            a=1
            b=1
    if n%2==0:
        sumatotal+=2*(n/2-r)+1
    else:
        sumatotal+=2*((n+1)/2-r)
    encontrado=0

print sumatotal
