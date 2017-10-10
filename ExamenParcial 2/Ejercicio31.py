#-*- coding:utf-8 -*-
#Primero crearemos nuestra variable que sumar� todos los n�meros
cantidad=0
#Luego crearemos una variable suma la cual nos dir� cuando una suma da la cantidad deseada.
SumaDeseada=200
#Ahora crearemos una variable temporal que tomar� los valores que vayamos sumando en las fichas
temporal=0
#ahora cada ficha recibir� un nombre espec�fico, por ejemplo las fichas 1 las nombraremos como e1, las de dos como e2, y as� seguiremos.

for e1 in range(0,201):
    temporal=e1
    if  temporal==200:
        cantidad+=1
    elif temporal<200:
        for e2 in range(0,201,2):
            temporal=e1+e2
            if temporal==200:
                cantidad+=1
            elif temporal<200:
                for e3 in range(0,201,5):
                    temporal=e1+e2+e3
                    if temporal==200:
                        cantidad+=1
                        temporal=temporal-e3
                    elif temporal<200:
                        for e4 in range(0,201,10):
                            temporal=e1+e2+e3+e4
                            if temporal==200:
                                cantidad+=1
                            elif temporal<200:
                                for e5 in range(0,201,20):
                                    temporal=e1+e2+e3+e4+e5
                                    if temporal==200:
                                        cantidad+=1
                                    elif temporal<200:
                                        for e6 in range(0,201,50):
                                            temporal=e1+e2+e3+e4+e5+e6
                                            if temporal==200:
                                                cantidad+=1
                                            elif temporal<200:
                                                for e7 in range(0,201,100):
                                                    temporal=e1+e2+e3+e4+e5+e6+e7
                                                    if temporal==200:
                                                        cantidad+=1
                                                    elif temporal<200:
                                                        for e8 in range(200,201,200):
                                                            temporal=e1+e2+e3+e4+e5+e6+e7+e8
                                                            if temporal==200:
                                                                cantidad+=1
#Lo que hace el programa es que va haciendo cada configuración, pero,
#en el momento en el que alguna se pasa simplemente continua hasta llegar al final
#de esta manera no se tarda tanto y solamente vamos guardando aquellos valores que den 200
print cantidad
