strongrepunit=[None]*200004
contador=1
strongrepunit.insert(1,0)
suma=0

for x in range (2,1000000):
  for y in range(2,50):
    j=(x**(y+1)-1)/(x-1)
    if(j>1000000000000):
      break
    elif(x<1000):
      for z in range(1,contador+2):
        if(j==strongrepunit[z]):
          break
        elif (z==contador+1):
          strongrepunit.insert(z,j)
          suma+=j
          contador+=1
    else:
      for z in range(1,contador+2):
        if(j==strongrepunit[z]):
          break
        elif (z==contador+1):
          suma+=j



print suma+1
