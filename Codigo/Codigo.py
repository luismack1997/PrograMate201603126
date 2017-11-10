#-*- coding:utf-8 -*-
'''
Created on 4/11/2017

@author: lm_lu
'''
import Tkinter
from PIL import ImageTk, Image
import os
import subprocess
import linecache
import sys
import json
import cPickle as pickle
import smtplib
import numpy as np
import matplotlib.pyplot as plt
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import re
import tkMessageBox
import time
from Tkinter import Studbutton

ruta=Tkinter.Tk()
ubicacionbitacora='bitacora.text'
ubicacionarchivo='archivo.text'
ubicacionjson='states_titlecase.json'
ubicacionlatex='pdfestados.tex'
ubicacionpdf='pdfestados.pdf'
ubicacionestaciones='stations.json'
ubicacionapedir='infoapedir.json'
ubicacionhtml='infohtml.html'
ubicaciongrafica='grafica.png'
ubicaciontemperatura='temperatura.json'
ubicacionfondo='Fondo.jpg'
ubicacionciudad='weather.json'

class Ubicacion():
    def ObtenerUbicaciones(self):
        global ubicacionarchivo
        ubicacionarchivo=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionarchivo
        global ubicacionbitacora
        ubicacionbitacora=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionbitacora
        global ubicacionjson
        ubicacionjson=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionjson
        global ubicacionlatex
        ubicacionlatex=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionlatex
        global ubicacionpdf
        ubicacionpdf=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionpdf
        global ubicacionestaciones
        ubicacionestaciones= ubicacionestaciones=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionestaciones
        global ubicacionhtml
        ubicacionhtml=os.path.dirname( os.path.realpath(__file__) )+"\\"+ubicacionhtml
        global ubicaciongrafica
        ubicaciongrafica=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicaciongrafica
        global ubicaciontemperatura
        ubicaciontemperatura=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicaciontemperatura
        global ubicacionfondo
        ubicacionfondo=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicacionfondo
        Interfaz().MenuPrincipal()
        global ubicacionciudad
        ubicacionciudad=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicacionciudad

class Usuario():
    def RevisarUsuario(self,valor,contra):
        temp=0
        fichero = open(ubicacionarchivo, 'r')
        if fichero.readline()=="":
            fichero.close()
            self.CrearUsuario(valor)
        else:
            num_lines = sum(1 for line in open(ubicacionarchivo))
            fichero.close()
            for x in range(1,num_lines+1):
                linea= linecache.getline(ubicacionarchivo, x)
                if valor==linea[:linea.index(" ")]:
                    os.system('CLS')
                    tkMessageBox.showinfo("Error", "El usuario ya existe pruebe crear otro diferente")
                    temp=1
                    break
                else:
                    temp=0
                linecache.clearcache()
        if temp==0:
            fichero.close()
            Interfaz().MenuCreacion(valor,contra)
        else:
            fichero.close()
                    
    def CrearUsuario(self, usuario,contra,correo):
        fichero = open(ubicacionarchivo, 'a')
        if (correo.count("@")>1 or correo.count("@")==0 or correo.count(".com")>1 or correo.count(".com")==0 or correo.index("@")>correo.index(".com")):
            os.system('CLS')
            tkMessageBox.showinfo("Error", "El correo que ingresó no es válido")
            subwin.destroy()
        else:
            temporal=usuario+" "+correo+" "+contra
            fichero.write(temporal) 
            fichero.write("\n")
            fichero.close()
            os.system('CLS')
            tkMessageBox.showinfo("Correcto", "Usuario creado correctamente")
            subwin.destroy()
                 
    def EncontrarUsuario(self, valor,contraIngresada):
        temp=0
        fichero=open(ubicacionarchivo, 'r')
        if fichero.readline()=="": 
            fichero.close()
            tkMessageBox.showinfo("Error", "No hay ningún usuario registrado con ese nombre")
        else: 
            num_lines=sum(1 for line in open(ubicacionarchivo))
            fichero.close()
            for x in range(1, num_lines+1):
                linea= linecache.getline(ubicacionarchivo, x)
                posiciones=[pos for pos, char in enumerate(linea) if char == " "]
                usuario=linea[:linea.index(" ")]
                correo=linea[linea.index(" ")+1:posiciones[1]]
                contra=linea[posiciones[1]+1:linea.index("\n")]
                if valor==correo or valor==usuario:
                    elecc=contraIngresada
                    if elecc!=contra:
                        temp=2
                        break
                    else:
                        temp=0
                        break
                else:
                    temp=1
        if temp==1:
            os.system('CLS')
            tkMessageBox.showinfo("Error", "No hay ningún usuario registrado con ese nombre")
        elif temp==2:
            tkMessageBox.showinfo("Error", "La contraseña no es correcta")
        else:
            os.system('CLS')
            Cierre().CrearBitacora(correo,usuario)
            ruta.destroy()
            Interfaz().MenuDatos()
                     
class Cierre():
    def CrearBitacora(self,correo,usuario):
        fichero=open(ubicacionbitacora, 'w')
        fichero.write("El siguiente es un documento con la información a la que usted accedió\n")
        temporal="Nombre de usuario: "+usuario+"\n"+"Correo: " +correo+"\n"
        fichero.write(temporal)
        fichero.write("A continuación se presenta una lista de los estados y las estaciones consultadas con su respectiva hora\n")
        s1="Estado*****"
        s2="Nombre*****"
        s3="Hora\n"
        s5='{:<20}{:<25}{:<}'.format(s1,s2,s3)
        fichero.write(s5)
        fichero.close()
                       
class Interfaz():
    
    def MenuPrincipal(self):
        img = ImageTk.PhotoImage(Image.open("MackTeck.png"))
        panel = Tkinter.Label(ruta, image = img)
        panel.pack(side = "bottom")
        ruta.geometry("450x360")
        ruta.title("Ingreso")
        label=Tkinter.Label(ruta, text="Bienvenido! Ingresa tu usuario o correo y tu contraseña")
        label.pack()
        label=Tkinter.Label(ruta, text="o de lo contrario crea un usuario.")
        label.pack()
        label=Tkinter.Label(ruta, text="Nombre de Usuario")
        label.pack()
        E1 = Tkinter.Entry(ruta, bd =5)
        E1.pack()
        label=Tkinter.Label(ruta, text="Contraseña")
        label.pack()
        E2 = Tkinter.Entry(ruta,show="*", bd =5)
        E2.pack()
        
        def Ingresar():
            input1=E1.get()
            input2=E2.get()
            if " " in input1  or " " in input2 or input1=="" or input2=="":
                tkMessageBox.showinfo("Error", "No ingrese espacios vacíos")
            else: 
                Usuario().EncontrarUsuario(input1,input2) 
                 
        def CrearUsuario():
            input1=E1.get()
            input2=E2.get()
            if " " in input1  or " " in input2 or input1=="" or input2=="":
                tkMessageBox.showinfo("Error", "No ingrese espacios vacíos")
                subwin.destroy()
            else: 
                Usuario().RevisarUsuario(input1,input2)
                
        botoningreso = Tkinter.Button(ruta, text="Ingresar", command=Ingresar)
        botoningreso.pack(side=Tkinter.LEFT,padx=110)
        botoningreso= Tkinter.Button(ruta, text="Crear Usuario", command=CrearUsuario)
        botoningreso.pack(side=Tkinter.LEFT,padx=10)
        
        ruta.mainloop()
    
    def MenuCreacion(self,valor,contra):
        def Registrar():
            correo=E1.get()
            if " " in correo  or correo=="":
                tkMessageBox.showinfo("Error", "No ingrese espacios vacíos")
                
            else: 
                Usuario().CrearUsuario(valor, contra, correo)
        global subwin
        subwin=Tkinter.Toplevel()  
        subwin.title("Registrar Usuario")
        subwin.geometry("300x100+120+120")
        label=Tkinter.Label(subwin, text="Correo: ").grid(row=0,column=0,padx=5,pady=5)
        E1=Tkinter.Entry(subwin,bd=5)
        E1.grid(row=0,column=1)
        botonIngresar=Tkinter.Button(subwin,text="Regístrame",command=Registrar).grid(row=1,column=0,padx=5,pady=5)
        
    def MenuDatos(self):
        ruta=Tkinter.Tk()
        def Decididor(selection):
            if selection=="Ver Estados": 
                Estados() 
            elif selection=="Mostrar Estaciones": 
                EstacionesDisponibles()
            else:
                MostrarCiudades()
                
        
        def Estados():
            Datos().MostrarEstados()
        def Estacion():
            print "so far so good"
        def EstacionesDisponibles():
            Datos().MostrarEstaciones()
        def CerrarSesion():
            print "so far so good"
        def Guardar():
            print "so far so good"
        def Ayuda():
            print "so far so good"
        def MostrarCiudades():
            print "so far so good"
        def Salir():
            ruta.destroy()
            
        def MiInfo():
            print "so far so good"
            
                   
        background_image=ImageTk.PhotoImage(Image.open("Fondo.jpg"))
        background_label = Tkinter.Label(ruta, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        ruta.title("Datos")
        ruta.geometry("545x465+0+0")
        
        menubar=Tkinter.Menu(ruta)
        menucomandos=Tkinter.Menu(menubar,tearoff=0)
        menucomandos.add_command(label="Ver Estados",command=Estados)
        menucomandos.add_command(label="Mostrar Estaciones", command=EstacionesDisponibles)
        menubar.add_cascade(label="Comandos",menu=menucomandos)
        
        menucierre=Tkinter.Menu(menubar,tearoff=0)
        menucierre.add_command(label="Cerrar Sesión", command=CerrarSesion)
        menucierre.add_command(label="Guardar", command=Guardar)
        menucierre.add_separator()
        menucierre.add_command(label="Salir",command=Salir)
        menubar.add_cascade(label="Cierre",menu=menucierre)
        
        menuayuda=Tkinter.Menu(menubar,tearoff=0)
        menuayuda.add_command(label="Acerca de",command=Ayuda)
        menubar.add_cascade(label="Ayuda", menu=menuayuda)
        ruta.configure(menu=menubar)
        
        label=Tkinter.Label(ruta, text="Bienvenido a la app del clima",bg='PeachPuff4').grid(row=0,column=1)
        label=Tkinter.Label(ruta,text="¿Qué desea hacer?",bg='PeachPuff4').grid(row=0,column=2)
        labelEstacion= Tkinter.Label(ruta, text="Ingresar Estación:",bg='PeachPuff4').grid(row=1,sticky=Tkinter.W,padx=5,pady=10)
        E1 = Tkinter.Entry(ruta, bd =5)
        E1.grid(row=1,column=1)
        labelEstacion=Tkinter.Label(ruta, text="Ingresar Estado:", bg='PeachPuff4').grid(row=3,column=0,padx=5,pady=10)
        E2=Tkinter.Entry(ruta,bd=5)
        E2.grid(row=3,column=1,padx=12)
        labelCiudad=Tkinter.Label(ruta,text="Ingresar Ciudad:", bg='PeachPuff4').grid(row=2,sticky=Tkinter.W, padx=5,pady=10)
        E3=Tkinter.Entry(ruta,bd=5)
        E3.grid(row=2,column=1)
        
        Comandos=["Ver Estados", "Mostrar Estaciones"] 
        TipoArchivo=Tkinter.StringVar()
        TipoArchivo.set(None)
        ComandosDown=Tkinter.OptionMenu(ruta,TipoArchivo,*Comandos,command=Decididor).grid(row=2,column=3,pady=10,padx=5)
        
        def InfoEstado():
            numero=E2.get()
            json_file=open(ubicacionjson,"r")
            estados=json.load(json_file)
            json_file.close()
            try:
                int(numero)
                if int(numero)<len(estados['results'])+1 and int(numero)>0:
                    Datos().MostarEstacionesPorEstados(estados['results'][int(numero)-1]["id"])
                else: 
                    tkMessageBox.showinfo("Error", "Debes ingresar números entre el 1 al 51, sin espacios.")
            except: 
                tkMessageBox.showinfo("Error", "Debes ingresar números entre el 1 al 51, sin espacios.")
        
        def Ciudad():
            nombre=E3.get( )
            Ciudades().MostrarDatos(nombre)
        botonEstado=Tkinter.Button(ruta,text="Info. Estado:",command=InfoEstado).grid(row=3,column=2)
        botonEstacion=Tkinter.Button(ruta,text="Info. Estación",command=Estacion).grid(row=1,column=2,padx=5)
        botonCiudad=Tkinter.Button(ruta,text="Info. Ciudad",command=Ciudad).grid(row=2,column=2,padx=5)
        botonGrafica=Tkinter.Button(ruta,text="Ver Mis Datos",command=MiInfo).grid(row=1,column=3,sticky=Tkinter.W)
        global Panel
        Panel=Tkinter.Text(ruta)
        Panel.config(width=60,height=15)
        Panel.grid_forget()
        ruta.mainloop()
        
class Datos():
    def MostrarEstados(self):
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=52\" >states_titlecase.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionjson,"r")
        estados=json.load(json_file)
        json_file.close()
        s1="Bienvenido, puedes bajar para ver el resto de texto\n"
        s2="Están ordenados por número, y nombre\n"
        s3="Si quieres ver las estaciones de un estado ingresa el número\n en la opción Consultar Estado y luego has click \n en el botón Info. Estado\n"
        Panel.delete(1.0,Tkinter.END)
        Panel.insert(Tkinter.END,s1)
        Panel.insert(Tkinter.END,s2)
        Panel.insert(Tkinter.END,s3)        
        
        for x in range(0,51):
            name=estados["results"][x]["name"]
            s1=str(x+1)+") "+name+"\n"
            Panel.insert(Tkinter.END,s1)
            Panel.grid(row=4,column=0,columnspan=6,sticky=Tkinter.W)
        
    def MostrarDatosdeEstacion(self,id):
        infoapedir=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations/"+id
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ infoapedir +"\" >infoapedir.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionapedir,"r")
        estacion=json.load(json_file)
        json_file.close()
        infoapedir2=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?stationin="+id
        cadenaCompilacion2 = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ infoapedir2 +"&limit=100\" >temperatura.json"
        subprocess.Popen(cadenaCompilacion2, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file2=open(ubicaciontemperatura,"r")
        estacion2=json.load(json_file2)
        json_file2.close()
        if "name" in estacion.keys():
            s1="Nombre: "+estacion["name"]
            #s2="Fecha Mínima: "+estacion["mindate"].decode('utf-8')
            #s3="Fecha Máxima: "+estacion["maxdate"]
            s4="Latitud: "+str(estacion["latitude"])
            s5="Cobertura de datos: "+str(estacion["datacoverage"])
            s6="Id: "+estacion["id"]
            #s7="Unidad de la Elevación: "+estacion["elevationUnit"]
            s8="Elevación: "+str(estacion["elevation"])
            #s9="longitud: "+str(estacion["logitude"])
            print s1
            #print s2
            #print s3
            print s4
            print s5
            print s6
            #print s7
            print s8
            #print s9
            print "A continuación le muestro los datos meteorológicos disponibles (100 es el límite)"
            print "Estos son los posibles datos que puede mostrar la estación, no todas los miden y tienen data"
            for x in range(0,len(estacion2['results'])):
                temporal=str(x+1)+") Nombre: "+estacion2["results"][x]["name"]+"*****Id: "+estacion2["results"][x]["id"]
                print temporal
            elecc=raw_input("Ingrese el número del dato que desea consultar o cualquier tecla para regresar\n")
            try:
                int(elecc)
                if int(elecc)>0 and int(elecc)<=len(estacion2['results']):
                    self.MostrarDatoEspecifico(id,estacion2["results"][int(elecc)-1]["id"])
                else: 
                    estado=estacion["name"][estacion["name"].index(",")+2:]
                    estado=estado[:estado.index(" ")]
                    nombre=estacion["name"][:estacion["name"].index(",")]
                    Cierre().AgregarDatos(estado, nombre)
                    os.system('CLS')
                    Menus().MenuDatos1() 
            except: 
                estado=estacion["name"][estacion["name"].index(",")+2:]
                estado=estado[:estado.index(" ")]
                nombre=estacion["name"][:estacion["name"].index(",")]
                Cierre().AgregarDatos(estado, nombre)
                os.system('CLS')
                Menus().MenuDatos1() 
        else:
            os.system('CLS')
            print "La estación que ingresó no es válida"
            Menus().MenuDatos1()
            
    def MostrarDatoEspecifico(self, id, dato):
        infoapedir=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes?stationid="+id+"&datacategoryid="+dato
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ infoapedir +"&limit=100\" >temperatura.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicaciontemperatura,"r")
        estacion=json.load(json_file)
        json_file.close()
        print "A continuación se muestran los datos disponibles que pediste (máx 100)"
        try: 
            for x in range(0,len(estacion["results"])):
                try:
                    print str(x+1)+") Nombre: "+estacion["results"][x]["name"], estacion["results"][x]["maxdate"]
                except: 
                    print str(x+1)+") Nombre: "+estacion["results"][x]["name"]
            raw_input("Preciona cualquier tecla para regresar")
            os.system('CLS')
            self.MostrarDatosdeEstacion(id)
        except: 
            os.system('CLS')
            print "Error 402, archivo no encontrado, no hay datos disponibles sobre esta categoría"
            raw_input("Preciona cualquier tecla para regresar")
            self.MostrarDatosdeEstacion(id)
        
    def MostarEstacionesPorEstados(self,id):
        estadoapedir=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?locationid="+id
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ estadoapedir +"&limit=1000\" >stations.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionestaciones,"r")
        estaciones=json.load(json_file)
        json_file.close()
        s1="Bienvenido, puedes bajar para ver el resto de texto\n"
        s2="Están ordenados por número, id, estado y nombre\n"
        s3="Si quieres saber más de alguna estación ingresa el id en la opción Ingresar Estación y luego presiona Info. Estación\n"
        Panel.delete(1.0,Tkinter.END)
        Panel.insert(Tkinter.END,s1)
        Panel.insert(Tkinter.END,s2)
        Panel.insert(Tkinter.END,s3)
        for x in range(0,len(estaciones['results'])):
            s1=str(x+1)+") "+estaciones["results"][x]["id"]+" "+estaciones["results"][x]["name"]+"\n"
            Panel.insert(Tkinter.END,s1)
            Panel.grid(row=4,column=0,columnspan=6,sticky=Tkinter.W)
        
    def MostrarEstaciones(self):
        estadoapedir=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ estadoapedir+"?limit=1000\" >stations.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionestaciones,"r")
        estaciones=json.load(json_file)
        json_file.close()
        s1="Bienvenido, puedes bajar para ver el resto de texto\n"
        s2="Están ordenados por número, id, estado y nombre\n"
        s3="Si quieres saber más de alguna estación ingresa el id en la opción Ingresar Estación y luego presiona Info. Estación\n"
        Panel.delete(1.0,Tkinter.END)
        Panel.insert(Tkinter.END,s1)
        Panel.insert(Tkinter.END,s2)
        Panel.insert(Tkinter.END,s3)
        for x in range(0,len(estaciones['results'])):
            s1=str(x+1)+") "+estaciones["results"][x]["id"]+" "+estaciones["results"][x]["name"]+"\n"
            Panel.insert(Tkinter.END,s1)
            Panel.grid(row=4,column=0,columnspan=6,sticky=Tkinter.W)

class InformacionUsuario():
    def GuardadoTemporal(self,Ciudad):
        print "So far so good"
        
class Ciudades():
    def MostrarDatos(self,nombre):
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & curl \"http://api.openweathermap.org/data/2.5/weather?q="+nombre+"&APPID=2a08770d154f0d7863a50b5c924727b4\" >weather.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionciudad,"r")
        infociudad=json.load(json_file)
        json_file.close()
        if infociudad["cod"]=="404": 
            tkMessageBox.showinfo("Error 404", "Al parecer el nombre de tu ciudad no existe")
        elif infociudad["cod"]=="400":
            tkMessageBox.showinfo("Error 400", "Nada que buscar")
        else: 
            InformacionUsuario().GuardadoTemporal(nombre)
            subwin=Tkinter.Toplevel()  
            background_image=ImageTk.PhotoImage(Image.open("icono.png"))
            background_label = Tkinter.Label(subwin, image=background_image)
            background_label.place(x=50, y=10, relwidth=1, relheight=1)
            subwin.title("Información Ciudad")
            subwin.geometry("380x150+120+120")
            label=Tkinter.Label(subwin, text="Nombre: ").grid(row=0,column=0,padx=5,pady=5)
            s1=infociudad["name"]
            label=Tkinter.Label(subwin,text=s1).grid(row=0,column=1,padx=5)
            label=Tkinter.Label(subwin, text="Viento: ").grid(row=1,column=0,padx=5,pady=5)
            s1=str(infociudad["wind"]["speed"])+"Mph"
            label=Tkinter.Label(subwin, text=s1).grid(row=1,column=1,padx=5,pady=5)
            label=Tkinter.Label(subwin, text="Clima: ").grid(row=2,column=0,padx=5,pady=5)
            s1=infociudad["weather"][0]["main"]
            label=Tkinter.Label(subwin, text=s1).grid(row=2,column=1,padx=5,pady=5)
            icon=infociudad["weather"][0]["icon"]
            cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & curl \"http://openweathermap.org/img/w/" +icon+".png\" >icono.png"
            subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
            s1=time.ctime()
            label=Tkinter.Label(subwin, text="Fecha y Hora:").grid(row=0,column=2,padx=5,pady=5)
            label=Tkinter.Label(subwin, text=s1).grid(row=0,column=3,padx=5,pady=5)
            label=Tkinter.Label(subwin, text="Temperatura:").grid(row=1,column=2,padx=5,pady=5)
            s1=int(infociudad["main"]["temp"])-273.15
            s2=str(s1)+" (Celcius)"
            label=Tkinter.Label(subwin, text=s2).grid(row=1,column=3,sticky=Tkinter.W,padx=5,pady=5)
            label=Tkinter.Label(subwin,text="País: ").grid(row=3,column=0,padx=5,pady=5)
            s1=infociudad["sys"]["country"]
            label=Tkinter.Label(subwin,text=s1).grid(row=3,column=1,padx=5,pady=5)
            def Regresar():
                subwin.destroy()
            botonRegresar=Tkinter.Button(subwin,text="Regresar",command=Regresar).grid(row=3,column=2,padx=5)
            subwin.mainloop()
        

Ubicacion().ObtenerUbicaciones()