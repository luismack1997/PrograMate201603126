import math
Solutions=0
n=0

def divisors(n):
    divs = [1]
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return list(set(divs))


for x in range(1,10):
    n=math.pow(10,x)    
    for y in range(1,x+1):
        z=1
        a=math.pow(5,z) 
        b=math.pow(2,y)       
        while n%a==0:
            if b<a:
                k=x-z
                j=x-y
                c=a+b
                while c%2==0 or c%5==0:
                    if c%2==0:
                        j+=1
                        c=c/2
                    else:
                        k+=1
                        c=c/5
                temporal=0
                for i in divisors(c):
                    temporal+=1
                Solutions+=(k+1)*(j+1)*temporal
            z+=1
            a=math.pow(5,z)
            
        z=1
        a=math.pow(2,z)
        b=math.pow(5,y)
        while n%a==0:
            if b<a:
                k=x-z
                j=x-y
                c=a+b
                while c%2==0 or c%5==0:
                    if c%2==0:
                        k+=1
                        c=c/2
                    else:
                        j+=1
                        c=c/5
                temporal=0
                for i in divisors(c):
                    temporal+=1
                Solutions+=(k+1)*(j+1)*temporal
            z+=1
            a=math.pow(2,z)
            
    z=0
    a=math.pow(2,z)
    while n%a==0:
        a=math.pow(2,z)
        y=0
        b=math.pow(5,y)
        while n%(a*b)==0:
            b=math.pow(5,y)
            k=x-z
            j=x-y
            c=1+a*b
            while c%2==0 or c%5==0:
                if c%2==0:
                    k+=1
                    c=c/2
                else:
                    j+=1
                    c=c/5
            temporal=0
            for i in divisors(c):
                temporal+=1
            Solutions+=(k+1)*(j+1)*temporal
            y+=1
        z+=1

    
print Solutions

        
        



