a=1900
mes=1
dia=1
diasem=1
contador=0
cambio=0

while a<=2000:
    if diasem==7 and dia==1 and a>1900:
        contador+=1

    if dia==28 and mes==2 and a/4!=0:
        dia=1
        cambio=1
        mes+=1
    if dia==29 and mes==2 and a/4==0:
        dia=1
        cambio=1
        mes+=1
    if dia==30 and (mes==4 or mes==11 or mes==6 or mes==9):
        dia=1
        cambio=1
        mes+=1
    if dia==31 and (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        dia=1
        cambio=1
        if mes==12:
            mes=1
        else:
            mes+=1

    if cambio==1:
        cambio=0
    else:
        dia+=1

    if diasem==7:
        diasem=1
    else:
        diasem+=1

    if mes==12 and dia==31:
        a+=1

    



print contador