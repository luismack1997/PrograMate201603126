#-*- coding:utf-8 -*-
import os
def PantallaPrincipal():
    print "¿Cuál figura desea ver?\n"
    figura=input("1) Triángulos\n2) Cuadrados \n3) Rectángulos\n")
    if(figura==1):
      os.system('cls')
      Triangulos()
    elif(figura==2):
      os.system('cls')
      Cuadrados()
    elif(figura==3):
      os.system('cls')
      Rectangulos()
    else:
        print "Ingreso no valido\n"
        Pantallaprincipal()



def Cuadrados():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2) Relleno\n")
    if(tipo==2):
      base=input("Ingrese la longitud del lado\n")
      for x in range(0,base):
        print "*"*base
    elif(tipo==1):
      base=input("Ingrese la longitud del lado\n")
      for x in range(0,base):
        if(x==0):
          print "*"*base
        elif(x<base-1):
          y=base-4
          print "*", " "*y,"*"
        else:
          print "*"*base
    else:
      os.system("cls")
      print "Ingreso no valido"
      Triangulos()
    pregunta=input("Otra figura? 1) Si\n(Cualquier tecla para salir)\n")
    if (pregunta==1):
      PantallaPrincipal()

def Triangulos():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2) Relleno\n")
    if(tipo==2):
      base=input("Ingrese la longitud de la base\n")
      for x in range(0,base+1):
        print "*"*x
    elif(tipo==1):
      base=input("Ingrese la longitud de la base\n")
      for x in range(0,base+1):
        if(x==0):
          print "*"
        elif(x==1):
          print "* *"
        elif(x<base):
          y=x-2
          print "*", " "*y,"*"
        else:
          y=x-1
          print "**", "*"*y
    else:
      print "*", " ", "*"*base
      print "Ingreso no valido"
      Triangulos()
    pregunta=input("Otra figura? 1) Si\n(Cualquier tecla para salir)\n")
    if (pregunta==1):
      os.system("cls")
      PantallaPrincipal()





def Rectangulos():
    tipo=input("Ingrese si lo quiere:\n 1) Hueco\n 2) Relleno\n")
    if(tipo==2):
      ancho=input("Ingrese la longitud del ancho\n")
      altura=input("Ingrese la longitud de la altura\n")
      for x in range(0,altura):
        print "*"*ancho
    elif(tipo==1):
      ancho=input("Ingrese la longitud del ancho\n")
      altura=input("Ingrese la longitud de la altura\n")
      for x in range(0,altura):
        if(x==0):
          print "*"*ancho
        elif(x<altura-1):
          y=ancho-4
          print "*", " "*y,"*"
        else:
          print "*"*ancho
    else:
      os.system("cls")
      print "Ingreso no valido"
      Triangulos()
    pregunta=input("Otra figura? 1) Si\n(Cualquier tecla para salir)\n")
    if (pregunta==1):
      os.system("cls")
      PantallaPrincipal()


PantallaPrincipal()
