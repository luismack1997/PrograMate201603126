import math
abundantespares=[0]*28124
abundantesimpares=[0]*28124
abundantes=[0]*28124
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
      print abundantespares[contadorpares]
      contadorpares+=1
  temporal=0

for x in range(2,30,2):
  suma+=x

suma+=34
suma+=46

for x in range(1,28125,2):
  suma+=x

for x in range(1,contadorimpares+1):
    for z in range(1,contadorpares+1):
        if(abundantesimpares[x]+abundantespares[z]>28124):
            break
        else:
            temporal=abundantespares[z]+abundantesimpares[x]
            if(temporal % 2==1):
                abundantes[temporal]=temporal

print suma

for x in range(1,28124):
    suma-=abundantes[x]

print suma-24
