import math
x=1010
encontrado=0
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
sumatotal=0
lista=[]

def recursivo(x):
    global n1, n2, n3, n4, n5, n6
    global p1, p2, p3, p4, p5, p6
    global sumatotal
    global lista
    if n1==1 and n2==1 and n3==1 and n4==1 and n5==1 and n6==1:
        lista2=[]
        lista2.append(p1)
        lista2.append(p2)
        lista2.append(p3)
        lista.append(p4)
        lista2.append(p5)
        lista2.append(p6)
        if len(lista) == len(set(lista)):
            sumatotal=p1*(p1+1)/2+p2*p2+p3*(3*p3-1)/2+p4*(2*p4-1)+p5(5*p5-3)/3+p6*(3*p6-2)
        else: 
            x=lista[0]
            n1=0
            n2=0
            n3=0
            n4=0
            n5=0
            n6=0
            if str(x)[2:]=="99": 
                recursivo(x+11)
            else:
                recursivo(x+1)

    elif n1<2 and n2<2 and n3<2 and n4<2 and n5<2 and n6<2: 
        p1=(-1+math.sqrt(1+8*x))/2
        p2=math.sqrt(x)
        p3=(1+math.sqrt(1+24*x))/6
        p4=(1+math.sqrt(1+8*x))/4
        p5=(3+math.sqrt(9+40*x))/10
        p6=(2+math.sqrt(4+12*x))/6
        if p1.is_integer():
            lista.append(x)
            n1+=1
            recursivo(   int(str(x)[2:]+"10")  )
        elif p2.is_integer():
            lista.append(x)
            n2+=1
            recursivo(   int(str(x)[2:]+"10")  )
        elif p3.is_integer():
            lista.append(x)
            n3+=1
            recursivo(   int(str(x)[2:]+"10")  )
        elif p4.is_integer():
            lista.append(x)
            n4+=1
            recursivo(   int(str(x)[2:]+"10")  )
        elif p5.is_integer():
            lista.append(x)
            n5+=1
            recursivo(   int(str(x)[2:]+"10")  )
        elif p6.is_integer():
            lista.append(x)
            n6+=1
        elif str(x)[2:]=="99": 
            try:
                x=lista[-1]
                del lista[-1]
                recursivo(x+11)
            except:
                recursivo(x+11)
        else:
            recursivo(x+1)
    else:
        x=lista[0]
        n1=0
        n2=0
        n3=0
        n4=0
        n5=0
        n6=0
        if str(x)[2:]=="99": 
            recursivo(x+11)
        else:
            recursivo(x+1)
recursivo(x)
print sumatotal

                                    



