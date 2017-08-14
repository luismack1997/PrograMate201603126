#-*- coding:utf-8 -*-
def PantallaPrincipal():
    print "¿Cuál figura desea obtener?\n"
    figura=input("1) Triángulos\n 2) Cuadrados \n 3) Rectángulos ")
    if(figura==1):
        Triangulos()
    elif(figura==2):
        Cuadrados()
    elif(figura==3):
        Rectangulos()
    else:
        print "Ingreso no valido\n"
        Pantallaprincipal()



def Cuadrados():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2)Relleno\n")

def Triangulos():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2)Relleno\n")
    if(tipo==1):
        base=input("Ingrese la longitud de la base\n")
        for x in range(0,base):
            if i == base-1:
				print "*"*base
            else:
                print "*"


def Rectangulos():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2)Relleno\n")


PantallaPrincipal()
