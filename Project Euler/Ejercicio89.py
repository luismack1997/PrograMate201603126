#solución problema por Luis E. Mack
#Lo primero que hay que hacer es cargar el texto en una variable nueva
fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio89.txt','r')

#Bien, vamos a guardar varias cosas importates, temporal, me guardará el dígito que acaba de salir, digito irá guardando el valor
#del número romano en entero y longitud será la cantidad de letras que usa dicho número

def romanos_decimal(texto):
    digito=0
    temporal=0
    longitud=0
    longitudnueva=0
#aquí vamos a analizar cada caracter de un número romano dado
    for caracter in texto:
#vamos analizando los casos, solo hay dos, si antes venía una variable más pequeña entonces debemos restarle al valor que queremos sumar
#a dicha variable, de lo contrario sumamos el valor que viene tal cual
        if caracter=='M':
            if temporal==100:
#sumamos 800 en vez de 900 por que cuando salió el valor 100 fue sumado y hacemos lo mismo para todos los demás
                digito+=800
                temporal=1000
#sumamos 1 por el caracter que apareció
                longitud+=1
            else: 
#si antes de mil no venía 100 entonces solamente lo sumamos
                digito+=1000
                temporal=1000
                longitud+=1
        elif caracter=='D':
            if temporal==100:
                digito+=300
                temporal=500
                longitud+=1
            else:
                digito+=500
                temporal=500
                longitud+=1
        elif caracter=='C':
            if temporal==10:
                digito+=80
                temporal=100
                longitud+=1
            else:
                digito+=100
                temporal=100
                longitud+=1
        elif caracter=='L':
            if temporal==10:
                digito+=30
                temporal=50
                longitud+=1
            else:
                digito+=50
                temporal=50
                longitud+=1
        elif caracter=='X':
            if temporal==1:
                digito+=8
                temporal=10
                longitud+=1
            else:
                digito+=10
                temporal=10
                longitud+=1
        elif caracter=='V':
            if temporal==1:
                digito+=3
                temporal=5
                longitud+=1
            else:
                digito+=5
                temporal=5
                longitud+=1
        elif caracter=='I': 
            temporal=1
            digito+=1
            longitud+=1
#y con el algoritmo anterior hemos convertido el número de romano a decimal
#ahora convertimos de nuevo a romanos y vemos cuánto estamos ahorrando, hacemos la conversión a lo estúpido y por casos
#es lógico y claro pensar que para obtener el romano con la menor cantidad de letras, debemos ir restando al número en decimal, el mayor
# número romano que podamos, de esta cuenta usaremos el mínimo número de letras
    while digito>0:
        if digito>=1000:
            digito-=1000
            longitudnueva+=1
        elif digito>=900:
            digito-=900
            longitudnueva+=2
        elif digito>=500:
            digito-=500
            longitudnueva+=1
        elif digito>=400:
            digito-=400
            longitudnueva+=2
        elif digito>=100:
            digito-=100
            longitudnueva+=1
        elif digito>=90:
            digito-=90
            longitudnueva+=2
        elif digito>=50:
            digito-=50
            longitudnueva+=1
        elif digito>=40:
            digito-=40
            longitudnueva+=2
        elif digito>=10:
            digito-=10
            longitudnueva+=1
        elif digito>=9:
            digito-=9
            longitudnueva+=2
        elif digito>=5:
            digito-=5
            longitudnueva+=1
        elif digito>=4:
            digito-=4
            longitudnueva+=2
        else: 
            digito-=1
            longitudnueva+=1  
#devolvemos el tamaño de los ahorrado
    aho=longitud-longitudnueva
    return aho

#leemos las lineas del archivo
b=fichero.readlines()
fichero.close()
ahorrados=0
for line in b:
#mandamos cada línea al autómata
    a=romanos_decimal(line)
#sumamos los que vamos ahorando
    ahorrados+=a
#imprimimos el resultado
print ahorrados