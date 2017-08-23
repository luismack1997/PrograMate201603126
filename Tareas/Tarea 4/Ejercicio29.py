numero=[None]*1000
contador=0
for x in range(1,7):
    for y in range(2,101):
        for z in range(0,contador+1):
            if(x*y==numero[z]):
                break
            elif(z==contador):
                numero.insert(contador,x*y)
                contador+=1
                print x*y



print contador
