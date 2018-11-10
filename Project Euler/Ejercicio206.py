"""fuerza bruta, toma como 30 min"""
import math
numero=0
for x1 in range(0,10):
    for x2 in range(0,10):
        for x3 in range(0,10):
            for x4 in range(0,10):
                for x5 in range(0,10):
                    for x6 in range(0,10):
                        for x7 in range(0,10):
                            for x8 in range(0,10):
                                a=math.sqrt( int( "1" + str(x1)+"2"+str(x2)+"3"+str(x3)+"4"+str(x4)+"5" +str(x5)+"6"+str(x6)+"7"+str(x7)+"8"+str(x8)+"9"  ))  
                                if a.is_integer():
                                    numero=a
                                    print numero

print str(numero)+"00"