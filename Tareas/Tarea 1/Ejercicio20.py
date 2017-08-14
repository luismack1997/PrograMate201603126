#-*- coding:utf-8 -*-
factorial=1
suma=0
for x in range(0,100):
    factorial=factorial*(x+1)
while factorial>0:
    suma+=factorial % 10
    factorial-=factorial % 10
    factorial/=10
print suma
