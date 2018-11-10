import math
listaTrian=[]
listaCuadr=[]
listaPenta=[]
listaHexa=[]
listaHepta=[]
listaOcto=[]
listaNoSalidos=[]
encontrado=0
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
x=0
temp=0
for x in range(1,200):
    a1=x*(x+1)/2
    a2=x*x
    a3=x*(3*x-1)/2
    a4=x*(2*x-1)
    a5=x*(5*x-3)/2
    a6=x*(3*x-2)
    if a1<10000 and a1>1010:
        listaTrian.append(a1)
    if a2<10000 and a2>1010:
        listaCuadr.append(a2)
    if a3<10000 and a3>1010:
        listaPenta.append(a3)
    if a4<10000 and a4>1010:
        listaHexa.append(a4)
    if a5<10000 and a5>1010:
        listaHepta.append(a5)
    if a6<10000 and a6>1010:
        listaOcto.append(a6)

x=0

def Encontrar(a):
    global n1, n2, n3, n4, n5, n6
    global listaCuadr
    global listaNoSalidos
    global listaPenta
    global listaHepta
    global listaHexa
    global listaOcto
    global encontrado
    global temp
    if listaNoSalidos==[]:
        p1=(-1+math.sqrt(1+8*n1))/2
        p2=math.sqrt(n2)
        p3=(1+math.sqrt(1+24*n3))/6
        p4=(1+math.sqrt(1+8*n4))/4
        p5=(3+math.sqrt(9+40*n5))/10
        p6=(2+math.sqrt(4+12*n6))/6
        lista=[]
        lista.append(p1)
        lista.append(p2)
        lista.append(p3)
        lista.append(p4)
        lista.append(p5)
        lista.append(p6)
        if len(lista) == len(set(lista)) and str(temp)[2:]==str(n1)[:2]:
            print n1, n2, n3, n4, n5, n6
            if encontrado==0:
                encontrado+=n1+n2+n3+n4+n5+n6
    else: 
        if 2 in listaNoSalidos:
            a1=a
            for x1 in listaCuadr:
                if str(a1)[2:]==str(x1)[:2]:
                    a=x1
                    n2=a
                    if len(listaNoSalidos)==1:
                        temp=x1
                    listaNoSalidos.remove(2)
                    Encontrar(a)
                    listaNoSalidos.append(2)
                    a=a1
        if 3 in listaNoSalidos:
            a2=a
            for x2 in listaPenta:
                if str(a)[2:]==str(x2)[:2]:
                    a=x2
                    n3=a
                    if len(listaNoSalidos)==1:
                        temp=x2
                    listaNoSalidos.remove(3)
                    Encontrar(a)
                    listaNoSalidos.append(3)
                    a=a2
        if 4 in listaNoSalidos:
            a3=a
            for x3 in listaHexa:
                if str(a)[2:]==str(x3)[:2] and listaNoSalidos!=[]:
                    a=x3
                    n4=a
                    if len(listaNoSalidos)==1:
                        temp=x3
                    listaNoSalidos.remove(4)                  
                    Encontrar(a)
                    listaNoSalidos.append(4)
                    a=a3
        if 5 in listaNoSalidos:
            a4=a
            for x4 in listaHepta:
                if str(a)[2:]==str(x4)[:2] and listaNoSalidos!=[]:
                    a=x4
                    n5=a
                    if len(listaNoSalidos)==1:
                        temp=x4
                    listaNoSalidos.remove(5)
                    Encontrar(a)
                    listaNoSalidos.append(5)
                    a=a4
        if 6 in listaNoSalidos: 
            a5=a
            for x5 in listaOcto:
                if str(a)[2:]==str(x5)[:2] and listaNoSalidos!=[]:
                    a=x5
                    n6=a
                    if len(listaNoSalidos)==1:
                        temp=x5
                    listaNoSalidos.remove(6) 
                    Encontrar(a)
                    listaNoSalidos.append(6)
                    a=a5
    
    
    

while encontrado==0:
    a=listaTrian[x]
    n1=a
    listaNoSalidos=[2,3,4,5,6]
    n2=0
    n3=0
    n4=0
    n5=0
    n6=0
    Encontrar(a)
    x+=1
print encontrado