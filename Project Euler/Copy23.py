import math
abundantespares=[0]*28124
abundantesimpares=[0]*28124
suma=0
temporal=0
contadorpares=1
contadorimpares=1

for x in range(10,28124):
  for y in range(1,x):
    if(x % y ==0):
      temporal+=y
  if(temporal>x):
    if(x%2==1):
      abundantesimpares.insert(contadorimpares,x)
      contadorimpares+=1
    else:
      abundantespares.insert(contadorpares,x)
      contadorpares+=1
  temporal=0

for x in range(2,28,2):
  suma+=x

suma+=34

for x in range(1,28125,2):
  suma+=x

for x in range(947,28125,2):
    temporal=1
    while(temporal<contadorimpares+1):
        for z in range(1,contadorpares+1):
            if(abundantesimpares[temporal]+abundantespares[z]>x):
                temporal+=1
                break
        else:
            if(abundantesimpares[temporal]+abundantespares[z]==x):
                suma-=x
                temporal=contadorimpares+1
print suma
