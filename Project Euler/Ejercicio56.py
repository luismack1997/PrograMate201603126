elnumero=0
temporal1=0
temporal2=0

for x in range(1,100):
  for y in range(1,100):
    temporal1=x**y
    while(temporal1>0):
      temporal2+=temporal1 % 10
      temporal1=(temporal1-(temporal1 % 10) )/10
    if(temporal2>elnumero):
      elnumero=temporal2
      temporal2=0
    else:
      temporal2=0

print elnumero
