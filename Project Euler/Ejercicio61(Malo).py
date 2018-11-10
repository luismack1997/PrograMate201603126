import math
x=1010
encontrado=0
p1=0
n2=0
p2=0
n3=0
p3=0
n4=0
p4=0
n5=0
p5=0
n6=0
p6=0
n1=""
while encontrado==0:
    p1=(-1+math.sqrt( 1+8*x)   )/2
    if p1.is_integer():
        for x1 in range(10,100):
            n2=int(str(x)[2:]+str(x1))
            p2=math.sqrt(n2)
            if p2.is_integer():
                for x2 in range(10,100):
                    n3=int(str(n2)[2:]+str(x2))
                    p3=(1+math.sqrt(1+24*n3)   )/6
                    if p3.is_integer(): 
                        for x3 in range(10,100):
                            n4=int(str(n3)[2:]+str(x3))
                            p4=(1+math.sqrt( 1+8*n4)   )/4
                            if p4.is_integer():
                                for x4 in range(10,100):
                                    n5=int(str(n4)[2:]+str(x4))
                                    p5=(3+math.sqrt( 9+40*n5)   )/10
                                    if p5.is_integer():
                                        for x5 in range(10,100):
                                            n6=int(str(n5)[2:]+str(x5))
                                            p6=(2+math.sqrt(4+12*n6))/6
                                            n1=str(n6)[2:]
                                            if p6.is_integer() and n1==str(x)[:2]:
                                                lista=[]
                                                lista.append(p1)
                                                lista.append(p2)
                                                lista.append(p3)
                                                lista.append(p4)
                                                lista.append(p5)
                                                lista.append(p6)
                                                if len(lista) == len(set(lista)):
                                                    encontrado=1
                                                    sumatotal=x+n2+n3+n4+n5+n6
                                                    print x, p1
                                                    print n2, p2
                                                    print n3, p3
                                                    print n4, p4
                                                    print n5, p5
                                                    print n6, p6
    if int(str(x)[2:])==99:
        x+=11
    else:
        x+=1
print sumatotal

                                    
