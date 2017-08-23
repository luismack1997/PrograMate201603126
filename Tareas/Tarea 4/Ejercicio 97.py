contador=1
numero=2

while (contador<7830457):
  numero=(numero*2) %10000000000
  contador+=1

print (numero*28433) % 10000000000 +1
