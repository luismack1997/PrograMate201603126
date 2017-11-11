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
ubicacionbitacora2='bitacora2.text'
ubicaciongrafica2='grafica2.png'
lineasbit1=5
lineasbit2=0

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
        global ubicacionbitacora2
        ubicacionbitacora2=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicacionbitacora2
        global ubicaciongrafica2
        ubicaciongrafica=os.path.dirname(os.path.realpath(__file__))+"\\"+ubicaciongrafica2

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
            global subwin
            subwin.destroy()
        else:
            temporal=usuario+" "+correo+" "+contra
            fichero.write(temporal) 
            fichero.write("\n")
            fichero.close()
            os.system('CLS')
            tkMessageBox.showinfo("Correcto", "Usuario creado correctamente")
            global subwin
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
        fichero2=open(ubicacionbitacora2,"w")
        fichero2.write("")
        fichero2.close()
        lineasbit1=5 
        lineasbit2=0
           
    def AgregarDatos(self,estado,nombre):
        fichero=open(ubicacionbitacora, 'a')
        s1=estado+"  "+nombre+"  "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n"
        fichero.write(s1)
        fichero.close()
    
    def MandarCorreo(self,SC):
        temporal=linecache.getline(ubicacionbitacora, 3)
        temporal=temporal[temporal.index(" ")+1:temporal.rindex("\n")]
        linecache.clearcache()
        msg = MIMEMultipart()
        msg['From'] = 'appmack@hotmail.com'
        msg['To'] = temporal
        msg['Subject'] = 'No Contestar'

        body = 'ESTACIONES CONSULTADAS'
        msg.attach(MIMEText(body,'plain'))

        filename1=ubicacionpdf
        filename2=ubicacionhtml
        filename3=ubicaciongrafica
        attachment  =open(filename1,'rb')
        attachment2 =open(filename2,'rb')
        attachment3 =open(filename3,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        part2 = MIMEBase('application','octet-stream')
        part2.set_payload((attachment2).read())
        part3 = MIMEBase('application','octet-stream')
        part3.set_payload((attachment3).read())
        encoders.encode_base64(part)
        encoders.encode_base64(part2)
        encoders.encode_base64(part3)
        part.add_header('Content-Disposition',"attachment; filename= "+filename1)
        msg.attach(part)
        part2.add_header('Content-Disposition',"attachment; filename= "+filename2)
        msg.attach(part2)
        part3.add_header('Content-Disposition',"attachment; filename= "+filename3)
        msg.attach(part3)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.live.com',587)
        server.starttls()
        #server.login('appmack@hotmail.com','SOYUNROBOT123')
        #server.sendmail('appmack@hotmail.com',temporal,text)
        server.quit()
            
    def CrearGrafica(self,SC):
        num_lines = sum(1 for line in open(ubicacionbitacora))
        lista=[]
        contador=[]
        nombre=[]
        fichero2=open(ubicacionbitacora, 'r')
        fichero = open(ubicaciongrafica, 'w')
        for x in range(1,num_lines+1):
            temporal=linecache.getline(ubicacionbitacora, x)
            if num_lines>5 and x>5: 
                posiciones= [m.start() for m in re.finditer('  ', temporal)]
                temporal2=temporal[:posiciones[1]]
                if temporal2 not in lista: 
                    lista.append(temporal2)
                    contador.append("1")
                else: 
                    contador[lista.index(temporal2)]=str(int(contador[lista.index(temporal2)])+1)
        if num_lines>5:
            for x in range(0,len(lista)):
                nombre.append(lista[x][lista[x].index("  ")+2:])
        if num_lines>5: 
            y_pos=np.arange(len(nombre))
            plt.bar(y_pos, contador, align='center')
            plt.xticks(y_pos,nombre)
            plt.ylabel('Veces Consultadas')
            plt.xlabel('Nombre')
            plt.title('Estaciones')
            plt.savefig(ubicaciongrafica)
        fichero2.close()
        fichero.close()
        self.CreadorPdf(SC)
        
    def CreadorPdf(self,SC):
        fichero = open(ubicacionlatex, 'w')
        fichero.write('\\documentclass[11pt,twoside]{article}')
        fichero.write("\n")
        fichero.write('\\usepackage[utf8]{inputenc}')
        fichero.write('\n')
        fichero.write('\\usepackage[T1]{fontenc}')
        fichero.write('\n')
        fichero.write('\\usepackage[english,frenchb,spanish]{babel}')
        fichero.write('\n')
        fichero.write('\\usepackage{ifthen}')
        fichero.write('\n')
        fichero.write('\\def\localedef#1#2{')
        fichero.write('\n')
        fichero.write('\\ifthenelse{ \equal{\locale}{#1} }{')
        fichero.write('\n')
        fichero.write('\\selectlanguage{#2}')
        fichero.write('\n')
        fichero.write('\\expandafter\def\csname#1\endcsname ##1{##1}')
        fichero.write('\n')
        fichero.write(' }{')
        fichero.write('\n')
        fichero.write('\expandafter\def\csname#1\endcsname ##1{}')
        fichero.write('\n')
        fichero.write('  }')
        fichero.write('\n')
        fichero.write('}')
        fichero.write('\n')
        fichero.write('\\providecommand\locale{es}')
        fichero.write('\n')
        fichero.write('\\usepackage[margin=1in]{geometry}')
        fichero.write('\n')
        fichero.write('\\usepackage{fancyhdr}')
        fichero.write('\n')
        fichero.write('\\usepackage{amsfonts, amsmath, amssymb}')
        fichero.write('\n')
        fichero.write('\\usepackage[none]{hyphenat}')
        fichero.write('\n')
        fichero.write('\\usepackage{dsfont}')
        fichero.write('\n')
        fichero.write('\\usepackage{multirow}')
        fichero.write('\n')
        fichero.write('\\usepackage{graphicx}')
        fichero.write('\n')
        temporal='\\graphicspath{ {'+os.path.dirname(os.path.realpath(__file__))+'}}'
        fichero.write(temporal)
        fichero.write('\n')
        fichero.write('\\pagestyle{fancy}')
        fichero.write('\n')
        fichero.write('\\fancyhf{}')
        fichero.write('\n')
        fichero.write('\\fancyfoot{}')
        fichero.write('\n')
        fichero.write('\\cfoot{\\thepage}')
        fichero.write('\n')
        fichero.write('\\lhead{MackTeck}')
        fichero.write('\n')
        fichero.write('\\rhead{\\today}')
        fichero.write('\n')      
        fichero.write("\\begin{document}")
        fichero.write('\n')
        fichero.write("\\begin{center}")
        fichero.write('\n')
        fichero.write("\\textbf{{\LARGE Datos Consultados}}\\")
        fichero.write('\n')
        fichero.write("\\end{center}")
        fichero.write('\n')
        fichero.write("\\section*{Información:}")
        fichero.write('\n')
        fichero2=open(ubicacionbitacora, 'r')
        num_lines = sum(1 for line in open(ubicacionbitacora))
        lista=[]
        contador=[]
        hora=[]
        for x in range(1,num_lines+1):
            temporal=linecache.getline(ubicacionbitacora, x)
            if x==3 or x==2:
                temporal=temporal.replace(" "," $ ")
                temporal=temporal.replace("\n","$\n")
                temporal=temporal+"\\\\"
                fichero.write(temporal)
            elif x==1 or x==4: 
                fichero.write(temporal)
                fichero.write("\\\\")
                fichero.write("\n")
            elif x==5:
                fichero.write("\\begin{center}")
                fichero.write('\n')
                fichero.write("\\begin{tabular}{| c| c | c| c|c|}")
                fichero.write('\n')
                fichero.write("\\hline")
                fichero.write('\n')
                fichero.write("Estados & Estaciones & Hora & Veces Consultadas\\\\ ")
                fichero.write('\n')
                fichero.write("\\hline\\hline")
                fichero.write('\n')
                fichero.write("\\multirow{4}{10em}\\\\")
                fichero.write('\n')
            if (num_lines==5 and x==5):
                fichero.write("N/A & N/A & N/A & N/A\\\\")
                fichero.write('\n')
                fichero.write("\\hline")
                fichero.write('\n')
            elif num_lines>5 and x>5: 
                posiciones= [m.start() for m in re.finditer('  ', temporal)]
                temporal2=temporal[:posiciones[1]]
                if temporal2 not in lista: 
                    lista.append(temporal2)
                    hora.append(temporal[posiciones[1]+1:temporal.index("\n")])
                    contador.append("1")
                else: 
                    contador[lista.index(temporal2)]=str(int(contador[lista.index(temporal2)])+1)
        if num_lines>5:
            for x in range(0,len(lista)):
                estado=lista[x][:lista[x].index("  ")]
                nombre=lista[x][lista[x].index("  ")+2:]
                linea=estado+" & "+nombre+" & "+hora[x]+" & "+ contador[x]+"\\\\" 
                fichero.write(linea)
                fichero.write('\n')
                fichero.write("\\hline")
                fichero.write('\n')
        fichero.write("\\end{tabular}")
        if num_lines>5: 
            fichero.write("\\section*{Gráfica}")
            fichero.write("\n")
            fichero.write("A continuación se presenta una gráfica con lo que consultó")
            fichero.write("\n")
            fichero.write("\\includegraphics{grafica.png}")
            fichero.write("\n")
        fichero.write("\n")
        fichero.write("\\end{center}")
        fichero.write("\n")
        fichero.write('\\end{document}')
        linecache.clearcache()
        fichero.close()
        fichero2.close()
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & pdflatex  pdfestados.tex"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        self.CreadorHtml(SC)
    
    def CreadorHtml(self,SC):
        fichero = open(ubicacionhtml, 'w')
        fichero.write('<!DOCTYPE html>')
        fichero.write("\n")
        fichero.write('<html>')
        fichero.write("\n")
        fichero.write('<head>')
        fichero.write("\n")
        fichero.write('<meta charset=\"utf-8\">')
        fichero.write("\n")
        fichero.write('<title>Página web Programación Matemática</title>')
        fichero.write("\n")
        fichero.write(' </head>')
        fichero.write("\n")
        fichero.write('<body>')
        fichero.write("\n")
        fichero.write('<h1>  Información </h1>')
        fichero.write("\n")
        fichero.write('<p> El siguiente es un documento con la información a la que usted accedió </p>')
        fichero.write("\n")
        fichero.write('<ul>')
        fichero.write("\n")
        fichero2=open(ubicacionbitacora, 'r')
        num_lines = sum(1 for line in open(ubicacionbitacora))
        for x in range(2,num_lines+1):
            temporal=linecache.getline(ubicacionbitacora, x)
            if x==3 or x==2 or x==4:
                temporal2="<li>"+temporal+"</li>"
                fichero.write(temporal2)
                fichero.write("\n")
            if x==5:
                fichero.write('</ul>')
                fichero.write("\n")
            if num_lines>5 and x==5:
                fichero.write('<ol>')
                fichero.write("\n")
            if num_lines>5 and x>=5:
                temporal2="<li>"+temporal+"</li>"
                fichero.write(temporal2)
                fichero.write("\n")
        if num_lines>5: 
            fichero.write('</ol>')
            fichero.write('\n')
        if num_lines>5: 
            fichero.write('<p> A continuación se muestra la gráfica de lo consultado </p>')
            fichero.write('\n')
            temporal3='<img src=\"'+ubicaciongrafica+'\"/>'
            fichero.write(temporal3)
            fichero.write('\n')  
        fichero.write('</body>')
        fichero.write('\n')
        fichero.write('</html>')
        fichero.write('\n')
        fichero.close()
        fichero2.close()
        self.MandarCorreo(SC)
                         
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
                global subwin
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
                
        def Estados():
            Datos().MostrarEstados()
        def EstacionesDisponibles():
            Datos().MostrarEstaciones()
        def CerrarSesion():
            Cierre().CrearGrafica("C")
            ruta.destroy()
            Interfaz().MenuPrincipal()
            
        def Guardar():
            InformacionUsuario().Guardar()
        def Ayuda():
            tkMessageBox.showinfo("Ayuda", "Aquí debería poner ayuda si en caso que no presentara")
        def Salir():
            Cierre().CrearGrafica("S")
            ruta.destroy() 
        def MiInfo():
            InformacionUsuario().PerfilUsuario()
            
                   
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
            
        def Estacion():
            id=E1.get()
            Datos().MostrarDatosdeEstacion(id)
            
        botonEstado=Tkinter.Button(ruta,text="Info. Estado",command=InfoEstado).grid(row=3,column=2)
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
            estado=estacion["name"][estacion["name"].index(",")+2:]
            estado=estado[:estado.index(" ")]
            nombre=estacion["name"][:estacion["name"].index(",")]
            Cierre().AgregarDatos(estado, nombre)
            subwin2=Tkinter.Toplevel()  
            subwin2.title("Información Estación")
            subwin2.geometry("450x250+120+120") 
            label=Tkinter.Label(subwin2, text="Nombre: ").grid(row=0,column=0,padx=5,pady=5)
            s1=estacion["name"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=0,column=1,padx=5)
            label=Tkinter.Label(subwin2, text="Id: ").grid(row=0,column=2,padx=5,pady=5)
            s1=estacion["id"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=0,column=3,padx=5)
            label=Tkinter.Label(subwin2, text="Fecha Mínima: ").grid(row=1,column=0,padx=5,pady=5)
            s1=estacion["mindate"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=1,column=1,padx=5)
            label=Tkinter.Label(subwin2, text="Fecha Máxima: ").grid(row=1,column=2,padx=5,pady=5)
            s1=estacion["maxdate"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=1,column=3,padx=5)
            label=Tkinter.Label(subwin2, text="Covertura de Datos: ").grid(row=2,column=0,padx=5,pady=5)
            s1=estacion["datacoverage"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=2,column=1,padx=5)
            label=Tkinter.Label(subwin2, text="Unidad Elevación: ").grid(row=2,column=2,padx=5,pady=5)
            s1=estacion["elevationUnit"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=2,column=3,padx=5)
            label=Tkinter.Label(subwin2, text="Elevación: ").grid(row=3,column=0,padx=5,pady=5)
            s1=estacion["elevation"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=3,column=1,padx=5)
            label=Tkinter.Label(subwin2, text="Longitud: ").grid(row=3,column=2,padx=5,pady=5)
            s1=estacion["longitude"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=3,column=3,padx=5)
            label=Tkinter.Label(subwin2, text="Latitud: ").grid(row=4,column=0,padx=5,pady=5)
            s1=estacion["latitude"]
            label=Tkinter.Label(subwin2,text=s1).grid(row=4,column=1,padx=5)
            def Regresar():
                subwin2.destroy()
            botonRegresar=Tkinter.Button(subwin2,text="Regresar",command=Regresar).grid(row=4,column=2,padx=5)
            subwin2.mainloop()
        else:
            tkMessageBox.showinfo("Error 400", "No hay información de esa estación, para buscar, pon el id nada más\n Ej: COOP:010008")
        
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
    def GuardadoTemporal(self,Ciudad,Pais,Temperatura):
        fichero=open(ubicacionbitacora2, 'a')
        s1=Ciudad+" "+Pais+"  "+Temperatura+"\n"
        fichero.write(s1)
        fichero.close()
    
    def Guardar(self):
        Bool=False
        global lineasbit1
        global lineasbit2
        fichero1=open(ubicacionbitacora, 'r')
        num_lines1 = sum(1 for line in open(ubicacionbitacora))
        fichero1.close()
        fichero2=open(ubicacionbitacora2, 'r')
        num_lines2=sum(1 for line in open(ubicacionbitacora2))
        fichero2.close()
        temporal=linecache.getline(ubicacionbitacora, 2)
        temporal2=linecache.getline(ubicacionbitacora, 3)
        Nombre=temporal[(temporal.index(":")+2):temporal.index("\n")]
        Correo=temporal2[(temporal2.index(":")+2):temporal2.index("\n")]
        linecache.clearcache()
        s1=os.path.dirname( os.path.realpath(__file__) )+"\\"+Nombre+".text"
        if os.path.isfile(s1)==False:
            fichero=open(s1, 'w')
            fichero.write(Nombre)
            fichero.write("\n")
            fichero.write(Correo)
            fichero.write("\n")
            fichero.write("Las estaciones están ordenadas por estado, nombre y veces consultadas\n")
            fichero.write("Mientras que las ciudades están ordenadas por \n ciudad, país y veces consultadas\n\n")
            fichero.close()
        if num_lines1>lineasbit1 or num_lines2>lineasbit2:
            fichero=open(s1, 'a')
            s1="Fecha y Hora de Guardado: "+time.ctime()+"\n"
            fichero.write(s1)
        if num_lines1>lineasbit1:
            lista=[]
            contador=[]
            fichero.write("Estaciones Consultadas:\n")
            for x in range(lineasbit1+1,num_lines1+1):
                temporal=linecache.getline(ubicacionbitacora, x)
                linecache.clearcache()
                posiciones= [m.start() for m in re.finditer('  ', temporal)]
                temporal2=temporal[:posiciones[1]]
                if temporal2 not in lista: 
                    lista.append(temporal2)
                    contador.append("1")
                else: 
                    contador[lista.index(temporal2)]=str(int(contador[lista.index(temporal2)])+1)
            for x in range(0,len(lista)):
                estado=lista[x][:lista[x].index("  ")]
                nombre=lista[x][lista[x].index("  ")+2:]
                linea=estado+" "+nombre+" "+ contador[x]+"\n" 
                fichero.write(linea)
            bool=True
            lineasbit1=num_lines1
           
            
        if num_lines2>lineasbit2:
            lista=[]
            contador=[]
            fichero.write("Ciudades:\n")
            for x in range(lineasbit2+1,num_lines2+1): 
                temporal=linecache.getline(ubicacionbitacora2, x)
                linecache.clearcache()
                temporal2=temporal[:temporal.index("  ")]
                if temporal2 not in lista: 
                    lista.append(temporal2)
                    contador.append("1")
                else: 
                    contador[lista.index(temporal2)]=str(int(contador[lista.index(temporal2)])+1)
            for x in range(0,len(lista)):
                linea=lista[x]+" "+ contador[x]+"\n" 
                fichero.write(linea)
            lineasbit2=num_lines2
            bool=True
        if bool:
            fichero.write("\n")
            fichero.close()
        tkMessageBox.showinfo("Listo", "Se han Guardado tus datos")
    
    def PerfilUsuario(self):
        subwin=Tkinter.Toplevel()
        subwin.title("Información Usuario")
        subwin.geometry("450x450+100+100")
        fichero1=open(ubicacionbitacora, 'r')
        fichero1.close()
        fichero2=open(ubicacionbitacora2, 'r')
        fichero2.close()
        temporal=linecache.getline(ubicacionbitacora, 2)
        temporal2=linecache.getline(ubicacionbitacora, 3)
        Nombre=temporal[(temporal.index(":")+2):temporal.index("\n")]
        Correo=temporal2[(temporal2.index(":")+2):temporal2.index("\n")]
        linecache.clearcache()
        label=Tkinter.Label(subwin, text="Nombre: ").grid(row=0,column=0,sticky=Tkinter.W,padx=5,pady=5)
        label=Tkinter.Label(subwin,text=Nombre).grid(row=0,column=1,padx=5,pady=5)
        label=Tkinter.Label(subwin,text="Correo").grid(row=0,column=2,sticky=Tkinter.W,padx=5,pady=5)
        label=Tkinter.Label(subwin,text=Correo).grid(row=0,column=3,padx=5,pady=5)
        def Consultas():
            self.MostrarConsultas(Nombre,Correo)
        def GEstaciones():
            Graficas().GraficaEstaciones()
        def GCiudades():
            Graficas().GraficaCiudades()
        def Regresar():
            subwin.destroy()
        global Panel2
        Panel2=Tkinter.Text(subwin)
        Panel2.config(width=50,height=15)
        Panel2.grid_forget()
        botonConsultas=Tkinter.Button(subwin,text="Mis Consultas",command=Consultas).grid(row=1,column=0,padx=5)
        botonGraficaEstaciones=Tkinter.Button(subwin,text="G. Estaciones",command=GEstaciones).grid(row=1,column=1,padx=5)
        botonGraficaCiudades=Tkinter.Button(subwin,text="G. Ciudades",command=GCiudades).grid(row=1,column=2,padx=5)
        botonRegresar=Tkinter.Button(subwin,text="Regresar",command=Regresar).grid(row=1,column=3,padx=5)
        
        subwin.mainloop()
    
    def MostrarConsultas(self,Nombre,Correo):
        Panel2.delete(1.0,Tkinter.END)
        linecache.clearcache()
        s1=os.path.dirname( os.path.realpath(__file__) )+"\\"+Nombre+".text"
        if os.path.isfile(s1)==False:
            fichero=open(s1, 'w')
            fichero.write(Nombre)
            fichero.write("\n")
            fichero.write(Correo)
            fichero.write("\n")
            fichero.write("Las estaciones están ordenadas por estado, nombre y veces consultadas\n")
            fichero.write("Mientras que las ciudades están ordenadas por \n ciudad, país y veces consultadas\n\n")
            fichero.close()
            tkMessageBox.showinfo("Error", "Parece que no has guardado ninguna información.")  
        else: 
            lineas=num_lines=sum(1 for line in open(s1))
            if lineas==6: 
                tkMessageBox.showinfo("Error", "Parece que no has guardado ninguna información.")  
            else:
                for x in range(3,num_lines+1):
                    temporal=linecache.getline(s1, x)
                    Panel2.insert(Tkinter.END,temporal)
                    Panel2.grid(row=2,column=0,columnspan=5,sticky=Tkinter.W)
            
        
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
            InformacionUsuario().GuardadoTemporal(infociudad["name"],infociudad["sys"]["country"],str(int(infociudad["main"]["temp"])-273.15))
            subwin=Tkinter.Toplevel()  
            background_image=ImageTk.PhotoImage(Image.open("icono.png"))
            background_label = Tkinter.Label(subwin, image=background_image)
            background_label.place(x=50, y=10, relwidth=1, relheight=1)
            subwin.title("Información Ciudad")
            subwin.geometry("400x150+120+120")
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

class Graficas():
    def GraficaEstaciones(self):
        num_lines = sum(1 for line in open(ubicacionbitacora))
        lista=[]
        contador=[]
        nombre=[]
        fichero2=open(ubicacionbitacora, 'r')
        fichero = open(ubicaciongrafica, 'w')
        for x in range(1,num_lines+1):
            temporal=linecache.getline(ubicacionbitacora, x)
            if num_lines>5 and x>5: 
                posiciones= [m.start() for m in re.finditer('  ', temporal)]
                temporal2=temporal[:posiciones[1]]
                if temporal2 not in lista: 
                    lista.append(temporal2)
                    contador.append("1")
                else: 
                    contador[lista.index(temporal2)]=str(int(contador[lista.index(temporal2)])+1)
        if num_lines<=5:
            tkMessageBox.showinfo("Error", "Parece que no has consultado ninguna estación")  
        if num_lines>5:
            if len(lista)>10:
                for x in range(len(lista)-10,len(lista)):
                    nombre.append(lista[x][lista[x].index("  ")+2:])
            else:
                for x in range(0,len(lista)):
                    nombre.append(lista[x][lista[x].index("  ")+2:])
        if num_lines>5: 
            y_pos=np.arange(len(nombre))
            plt.bar(y_pos, contador, align='center')
            plt.xticks(y_pos,nombre)
            plt.ylabel('Veces Consultadas')
            plt.xlabel('Nombre')
            plt.title('Estaciones')
            plt.show()
        fichero2.close()
        fichero.close()
    
    def GraficaCiudades(self):
        num_lines = sum(1 for line in open(ubicacionbitacora2))
        lista=[]
        contador=[]
        promedio=[]
        nombre=[]
        fichero2=open(ubicacionbitacora2, 'r')
        fichero = open(ubicaciongrafica2, 'w')
        for x in range(1,num_lines+1):
            temporal=linecache.getline(ubicacionbitacora2, x)
            posiciones= [m.start() for m in re.finditer(' ', temporal)]
            temporal2=temporal[:posiciones[1]]
            if temporal2 not in lista: 
                    lista.append(temporal2)
                    print temporal[ (posiciones[len(posiciones)-2]):temporal.index("\n") ]
                    contador.append(temporal[ (posiciones[len(posiciones)-2]):temporal.index("\n") ])                                                                               
        if num_lines==0:
            tkMessageBox.showinfo("Error", "Parece que no has consultado ninguna ciudad")  
        else: 
            if len(lista)>10:
                for x in range(len(lista)-10,len(lista)):
                    nombre.append(lista[x])
            else:
                for x in range(0,len(lista)):
                    nombre.append(lista[x])
        if num_lines>0: 
            y_pos=np.arange(len(nombre))
            plt.bar(y_pos, contador, align='center')
            plt.xticks(y_pos,nombre)
            plt.ylabel('Temperatura')
            plt.xlabel('Nombre')
            plt.title('Ciudad')
            plt.show()
        fichero2.close()
        fichero.close()
   
        

Ubicacion().ObtenerUbicaciones()