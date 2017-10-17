#-*- coding:utf-8 -*-
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
        Menus().MenuPrincipal()

class Datos():
    def MostrarEstados(self):
        print "A continuación se presenta una lista de estados"
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ " & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=ST&limit=52\" >states_titlecase.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionjson,"r")
        estados=json.load(json_file)
        for x in range(0,50,2):
            name1=estados["results"][x]["name"]
            name2=estados["results"][x+1]["name"]
            s1=str(x+1)+") "+name1
            s2=str(x+2)+") "+name2
            print '{0:25}  {1}'.format(s1, s2)
            name=estados["results"][50]["name"]
        print "51) "+name
        elecc=raw_input("Ingrese 0 para regresar o el número de la estación que desea consultar\n")
        try:
            int(elecc)
        except:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostrarEstados()
        if int(elecc)==0:
            json_file.close()
            os.system('CLS')
            Menus().MenuDatos1()
        elif int(elecc)<52 and int(elecc)>0:
            os.system('CLS')
            self.MostarEstacionesPorEstados(estados["results"][int(elecc)-1]["id"])
            json_file.close()
        else:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostrarEstados()

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
        for x in range(0,len(estaciones['results'])):
            s1=str(x+1)+") "+estaciones["results"][x]["name"]
            print s1
        elecc=raw_input("Ingrese 0 para regresar o el número del estado que desea consultar\n")
        try:
            int(elecc)
        except:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostarEstacionesPorEstados(id)
        if int(elecc)==0:
            json_file.close()
            os.system('CLS')
            self.MostrarEstados()
        elif int(elecc)<len(estaciones['results'])+1 and int(elecc)>0:
            os.system('CLS')
            self.MostrarDatosdeEstacion(estaciones['results'][int(elecc)-1]["id"])
            json_file.close()
        else:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostarEstacionesPorEstados(id)

    def MostrarEstaciones(self):
        estadoapedir=" & curl -H \"token:SSlIaWEESJKxGWGWMIkXDcNAEcPPqMIi\" \"https://www.ncdc.noaa.gov/cdo-web/api/v2/stations"
        cadenaCompilacion = "cd " +  os.path.dirname( os.path.realpath(__file__) )+ estadoapedir+"?limit=1000\" >stations.json"
        subprocess.Popen(cadenaCompilacion, shell=True, stdout =subprocess.PIPE).stdout.read()
        json_file=open(ubicacionestaciones,"r")
        estaciones=json.load(json_file)
        json_file.close()
        for x in range(0,len(estaciones['results'])):
            s1=str(x+1)+") "+estaciones["results"][x]["name"]
            print s1
        elecc=raw_input("Ingrese 0 para regresar o el número de la estación que desea consultar\n")
        try:
            int(elecc)
        except:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostrarEstaciones()
        if int(elecc)==0:
            json_file.close()
            os.system('CLS')
            Menus().MenuDatos1()
        elif int(elecc)<len(estaciones['results'])+1 and int(elecc)>0:
            os.system('CLS')
            self.MostrarDatosdeEstacion(estaciones['results'][int(elecc)-1]["id"])
            json_file.close()
        else:
            os.system('CLS')
            print "No es una opción válida"
            json_file.close()
            self.MostrarEstaciones()


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

    def AgregarDatos(self,estado,nombre):
        fichero=open(ubicacionbitacora, 'a')
        s1=estado+"  "+nombre+"  "+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+"\n"
        fichero.write(s1)
        fichero.close()

    def MandarCorreo(self,COR):
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
        server.login('appmack@hotmail.com','SOYUNROBOT123')
        server.sendmail('appmack@hotmail.com',temporal,text)
        server.quit()
        if COR=="salir":
            sys.exit(0)
        else:
            Menus().MenuPrincipal()

    def CrearGrafica(self,COR):
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
        self.CreadorPdf(COR)

    def CreadorPdf(self,COR):
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
        self.CreadorHtml(COR)

    def CreadorHtml(self,COR):
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
        self.MandarCorreo(COR)

class Usuario():

    def RevisarUsuario(self, valor):
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
                    print "El usuario ya existe pruebe otro usuario"
                    temp=1
                    break
                else:
                    temp=0
                linecache.clearcache()
        if temp==1:
            fichero.close()
            Menus().MenuCreacion()
        else:
            fichero.close()
            self.CrearUsuario(valor)


    def CrearUsuario(self, usuario):
        fichero = open(ubicacionarchivo, 'a')
        correo=raw_input("Ingrese correo electrónico\n")
        contra=raw_input("Ingrese Contraseña\n")
        if (correo.count("@")>1 or correo.count("@")==0 or correo.count(".com")>1 or correo.count(".com")==0 or correo.index("@")>correo.index(".com")):
            os.system('CLS')
            print "El correo que ingresó no es válido"
            self.CrearUsuario(usuario)
        elif correo.find(" ")!=-1:
            os.system('CLS')
            print "Ingresó espacio vacío en el correo"
            self.CrearUsuario(usuario)
        elif contra.find(" ")!=-1:
            os.system('CLS')
            print "Ingresó espacio vacío en la contraseña"
            self.CrearUsuario(usuario)
        else:
            temporal=usuario+" "+correo+" "+contra
            fichero.write(temporal)
            fichero.write("\n")
            fichero.close()
            os.system('CLS')
            print "Usuario creado correctamente"
            Menus().MenuRegreso()

class Ingreso():

    def EncontrarUsuario(self, valor):
        temp=0
        fichero=open(ubicacionarchivo, 'r')
        if fichero.readline()=="":
            fichero.close()
            print "No hay ningún usuario registrado con dicho usuario,"
            print "considere crear uno."
            Menus().MenuRegreso()
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
                    elecc=raw_input("Ingrese contraseña\n")
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
            print "El usuario que ingresó no existe en los archivos"
            Menus().MenuRegreso()
        elif temp==2:
            print "La contraseña que ingresó no es correcta"
            print "¿Qué desea hacer?"
            print "1) Regresar"
            print "2) Volver a intentar"
            elecc2=raw_input("3) Salir\n")
            if elecc2=="":
                os.system("CLS")
                print "Regresando al menú principal"
                Menus().MenuPrincipal()
            elif int(elecc2)==1:
                os.system("CLS")
                Menus().MenuPrincipal()
            elif int(elecc2)==2:
                self.EncontrarUsuario(valor)
            elif int(elecc2)==3:
                sys.exit(0)
                execfile()
            else:
                os.system("CLS")
                print "Regresando al menú principal"
                Menus().MenuPrincipal()
        else:
            os.system('CLS')
            Cierre().CrearBitacora(correo,usuario)
            Menus().MenuDatos1()

class Menus():
    def MenuPrincipal(self):
        print "Bienvenido, ¿qué desea hacer?"
        print "1) Crear Usuario"
        print "2) Ingresar"
        elecc=raw_input("3) Salir\n")
        if elecc=="":
            os.system('CLS')
            print "Opción no válida"
            self.MenuPrincipal()
        if elecc== "1":
            os.system('CLS')
            self.MenuCreacion()
        elif elecc== "2":
            os.system('CLS')
            self.MenuIngreso()
        elif elecc== "3":
            sys.exit(0)
            execfile()
        else:
            os.system('CLS')
            print "Opción no válida"
            self.MenuPrincipal()

    def MenuCreacion(self):
        elecc=raw_input("Ingrese Usuario\n")
        if elecc=="":
            os.system('CLS')
            print "Nombre de Usuario no válido"
            self.MenuCreacion()
        elif elecc.find(" ")!=-1:
            os.system('CLS')
            print "Por favor no ingresar espacios vacíos"
            self.MenuCreacion()
        else:
            Usuario().RevisarUsuario(elecc)

    def MenuIngreso(self):
        elecc=raw_input("Ingrese nombre de usuario o correo electrónico\n")
        if elecc=="":
            os.system('CLS')
            print "Nombre de Usuario o Correo no válido"
            self.MenuIngreso()
        elif elecc.find(" ")!=-1:
            os.system('CLS')
            print "Por favor no ingresar espacios vacíos"
            self.MenuIngreso()
        else:
            Ingreso().EncontrarUsuario(elecc)

    def MenuRegreso(self):
        print("¿Qué desea hacer?")
        print "1) Regresar"
        elecc=raw_input("2) Salir\n")
        if elecc=="":
            os.system('CLS')
            print "No es una opción válida"
            self.MenuRegreso()
        if elecc=="1":
            os.system('CLS')
            self.MenuPrincipal()
        elif elecc=="2":
            sys.exit(0)
        else:
            print "No es una opción válida"
            self.MenuRegreso()

    def MenuDatos1(self):
        print("Bienvenido ¿Qué desea hacer?")
        print("1) Ver estados")
        print("2) Ingresar Estación")
        print("3) Mostrar estaciones disponibles (1000 es el límite)")
        print("4) Cerrar Sesión")
        elecc=raw_input("5) Salir\n")
        if elecc=="":
            os.system('ClS')
            print "No es una opción válida"
            self.MenuDatos1()
        elif elecc=="1":
            os.system('CLS')
            Datos().MostrarEstados()
        elif elecc=="2":
            os.system('CLS')
            elecc2=raw_input("Ingrese el id de la estación Ej: COOP:010008\n")
            Datos().MostrarDatosdeEstacion(elecc2)
        elif elecc=="3":
            os.system('CLS')
            Datos().MostrarEstaciones()
        elif elecc=="4":
            os.system('CLS')
            Cierre().CrearGrafica("cerrar")
        elif elecc=="5":
            os.system('CLS')
            Cierre().CrearGrafica("salir")
        else:
            print "No es una opción válida"
            self.MenuDatos1()

Ubicacion().ObtenerUbicaciones()
