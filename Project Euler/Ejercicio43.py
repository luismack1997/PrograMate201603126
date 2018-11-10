x=17
y=1
a1=""
a2=""
a3=""
a4=""
a5=""
a6=""
a7=""
repetidos=0
sumatotal=0
guardador=0

while x*y<1000:
    a1=""
    if x*y<100:
        a1="0"+str(x*y)
    else:
        a1=str(x*y)
    for x1 in range(0,10):
            a2=""
            a2=str(x1)+a1
            if int(a2[:3])%13==0:
                for x2 in range(0,10):
                    a3=""
                    a3=str(x2)+a2
                    if int(a3[:3])%11==0:
                        for x3 in range(0,10):
                            a4=""
                            a4=str(x3)+a3
                            if int(a4[:3])%7==0:
                                for x4 in range(0,10):
                                    a5=""
                                    a5=str(x4)+a4
                                    if int(a5[:3])%5==0:
                                        for x5 in range(0,10):
                                            a6=''
                                            a6=str(x5)+a5
                                            if int(a6[:3])%3==0:
                                                for x6 in range(0,10):
                                                    a7=""
                                                    a7=str(x6)+a6
                                                    if int(a7[:3])%2==0:
                                                        for x7 in range(0,10):
                                                            if (str(x7) in a7)==False:
                                                                repetidos+=1
                                                                guardador=x7
                                                        if repetidos==1:
                                                            a7=str(guardador)+a7
                                                            sumatotal+=int(a7)
                                                            print a7
                                                        repetidos=0
    y+=1                                                
    


print sumatotal

