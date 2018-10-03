import math
fichero=file('\Users\lm_lu\OneDrive\Documentos\GitHub\PrograMate201603126\Project Euler\Ejercicio42.txt','r')
b=fichero.read()
fichero.close()
dictt = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8',
    'I':'9','J':'10','K':'11','L':'12','M':'13','N':'14','O':'15','P':'16','Q':'17',
    'R':'18','S':'19','T':'20','U':'21','V':'22','W':'23','X':'24','Y':'25','Z':'26'
    }

triangulares=0
sumatemporal=0
a=str(b).split(',')
for word in a: 
    for letter in word:
        if letter in dictt: 
            sumatemporal=sumatemporal+int(dictt[letter])
    if (math.sqrt(1+8*sumatemporal)).is_integer():
        triangulares+=1
    sumatemporal=0


print triangulares 

