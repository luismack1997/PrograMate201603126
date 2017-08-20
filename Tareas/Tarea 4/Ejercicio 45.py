import math
numero=286
elnumero=0
temporal=0

while(elnumero==0):
  temporal=numero*(numero+1)/2
  a=(0.5+math.sqrt(0.25+6*temporal) )/3
  b=(1+math.sqrt(1+8*temporal) )/4
  if(a % 1==0 and b % 1==0):
    elnumero=temporal
  else:
    numero+=1

print elnumero
