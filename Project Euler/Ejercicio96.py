import os
fichero=file(os.path.dirname(os.path.realpath(__file__))+"\\Ejercicio96.txt","r")
matrizOriginal=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,]]
matriz=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
NoPosibles=[]
def Resolvedor(x,y):
    global matriz
    global NoPosibles
    encontrado=0
    Posibles=1
    for x1 in range(0,9):
        if matriz[x1][y]!=0:
            NoPosibles.append(matriz[x1][y])
    
    for y1 in range(0,9):
        if matriz[x][y1]!=0:
            NoPosibles.append(matriz[x][y1])
    
    if x%3==0:
        if y%3==0:
            if matriz[x+1][y+1]!=0:
                NoPosibles.append(matriz[x+1][y+1])
            if matriz[x+1][y+2]!=0:
                NoPosibles.append(matriz[x+1][y+2])
            if matriz[x+2][y+1]!=0:
                NoPosibles.append(matriz[x+2][y+1])
            if matriz[x+2][y+2]!=0:
                NoPosibles.append(matriz[x+2][y+2])
        elif y%3==1:
            if matriz[x+1][y-1]!=0:
                NoPosibles.append(matriz[x+1][y-1])
            if matriz[x+2][y-1]!=0:
                NoPosibles.append(matriz[x+2][y-1])
            if matriz[x+2][y+1]!=0:
                NoPosibles.append(matriz[x+2][y+1])
            if matriz[x+1][y+1]!=0:
                NoPosibles.append(matriz[x+1][y+1])
        else: 
            if matriz[x+1][y-1]!=0:
                NoPosibles.append(matriz[x+1][y-1])
            if matriz[x+1][y-2]!=0:
                NoPosibles.append(matriz[x+1][y-2])
            if matriz[x+2][y-1]!=0:
                NoPosibles.append(matriz[x+2][y-1])
            if matriz[x+2][y-2]!=0:
                NoPosibles.append(matriz[x+2][y-2])
    
    if x%3==1:
        if y%3==0:
            if matriz[x+1][y+1]!=0:
                NoPosibles.append(matriz[x+1][y+1])
            if matriz[x+1][y+2]!=0:
                NoPosibles.append(matriz[x+1][y+2])
            if matriz[x-1][y+1]!=0:
                NoPosibles.append(matriz[x-1][y+1])
            if matriz[x-1][y+2]!=0:
                NoPosibles.append(matriz[x-1][y+2])
        elif y%3==1:
            if matriz[x-1][y-1]!=0:
                NoPosibles.append(matriz[x-1][y-1])
            if matriz[x-1][y+1]!=0:
                NoPosibles.append(matriz[x-1][y+1])
            if matriz[x+1][y-1]!=0:
                NoPosibles.append(matriz[x+1][y-1])
            if matriz[x+1][y+1]!=0:
                NoPosibles.append(matriz[x+1][y+1])
        else: 
            if matriz[x-1][y-1]!=0:
                NoPosibles.append(matriz[x-1][y-1])
            if matriz[x-1][y-2]!=0:
                NoPosibles.append(matriz[x-1][y-2])
            if matriz[x+1][y-2]!=0:
                NoPosibles.append(matriz[x+1][y-2])
            if matriz[x+1][y-1]!=0:
                NoPosibles.append(matriz[x+1][y-1])
    
    if x%3==2:
        if y%3==0:
            if matriz[x-1][y+1]!=0:
                NoPosibles.append(matriz[x-1][y+1])
            if matriz[x-1][y+2]!=0:
                NoPosibles.append(matriz[x-1][y+2])
            if matriz[x-2][y+1]!=0:
                NoPosibles.append(matriz[x-2][y+1])
            if matriz[x-2][y+2]!=0:
                NoPosibles.append(matriz[x-2][y+2])
        elif y%3==1:
            if matriz[x-1][y-1]!=0:
                NoPosibles.append(matriz[x-1][y-1])
            if matriz[x-2][y-1]!=0:
                NoPosibles.append(matriz[x-2][y-1])
            if matriz[x-2][y+1]!=0:
                NoPosibles.append(matriz[x-2][y+1])
            if matriz[x-1][y+1]!=0:
                NoPosibles.append(matriz[x-1][y+1])
        else: 
            if matriz[x-1][y-1]!=0:
                NoPosibles.append(matriz[x-1][y-1])
            if matriz[x-1][y-2]!=0:
                NoPosibles.append(matriz[x-1][y-2])
            if matriz[x-2][y-1]!=0:
                NoPosibles.append(matriz[x-2][y-1])
            if matriz[x-2][y-2]!=0:
                NoPosibles.append(matriz[x-2][y-2])
    
    while encontrado==0:
        if Posibles not in NoPosibles:
            encontrado=1
        else:
            Posibles+=1
    NoPosibles=[]
    return Posibles

def Resolvedor2():
    global matriz
    global matrizOriginal
    x=0
    while x<9:
        y=0   
        while y<9:
            if matriz[x][y]==0:
                a=Resolvedor(x,y)
                if a==10:
                    restado=0
                    while restado==0:
                        if y>1:
                            if matrizOriginal[x][y-1]==0:
                                b1=matriz[x][y-1]
                                matriz[x][y-1]=0
                                restado=1
                                for z1 in range(1,b1+1):
                                    NoPosibles.append(z1)
                                y-=2
                            else:
                                y-=1
                        elif y==1:
                            if matrizOriginal[x][y-1]==0:
                                b2=matriz[x][y-1]
                                matriz[x][y-1]=0
                                restado=1
                                for z2 in range(1,b2+1):
                                    NoPosibles.append(z2)
                                y=8
                                x-=1
                            else:
                                y-=1
                        else:
                            if matrizOriginal[x-1][8]==0:
                                b3=matriz[x-1][8]
                                matriz[x-1][8]=0
                                restado=1
                                for z3 in range(1,b3+1):
                                    NoPosibles.append(z3) 
                                y=7
                                x-=1
                            else: 
                                y=8
                                x-=1
                else:
                    matriz[x][y]=a
            y+=1        
        x+=1
    return int(str(matriz[0][0])+str(matriz[0][1])+str(matriz[0][2]))

contador=1
sumatotal=0
for line in fichero:
    if contador%10==1 and contador!=1:
        sumatotal+=Resolvedor2()
    elif contador!=1:
        for z in range(0,9):          
            matriz[(contador-2)%10][z]=int(line[z])
            matrizOriginal[(contador-2)%10][z]=int(line[z])
    contador+=1
#Sumamos el último sudoku que no se sumó. 
sumatotal+=Resolvedor2()

fichero.close()
print sumatotal