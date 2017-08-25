primo=[None]*100001
primo.insert(1,2)
contador=1
numero=3

#ingresamos los primos menores a 1,000,000
while(contador<100002):
    #inicio=time.time()
    for x in range(0,contador,1):
        if numero % primo[x+1]==0:
            numero+=1
            break
        elif x==contador-1:
            primo.insert(contador+1,numero)
            numero+=1
            contador+=1
            break
