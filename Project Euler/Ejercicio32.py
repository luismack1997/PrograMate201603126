sumatotal=0
total=""
lista=[]
for x in range(1,2000):
    for y in range(1,1000):
        total=str(x)+str(y)+str(x*y)
        if total.count("1")==1 and total.count("2")==1 and total.count("3")==1 and total.count("4")==1 and total.count("5")==1 and total.count("6")==1  and total.count("7")==1 and total.count("8")==1 and total.count("9")==1 and total.count("0")==0:
            if str(x*y) in lista: 
                pass
            else:
                lista.append(str(x*y))
                sumatotal+=x*y
                print x*y


print sumatotal

