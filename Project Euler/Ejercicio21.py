import math
suma=0
temporal1=0
temporal2=0

for x in range(1,10001):
  for y in range(1,x):
    if(x % y ==0):
      temporal1+=y
  for z in range(1,temporal1):
    if(temporal1 % z==0):
      temporal2+=z
  if(temporal2==x and temporal1!=x):
    suma+=x
  temporal1=0
  temporal2=0

print suma
