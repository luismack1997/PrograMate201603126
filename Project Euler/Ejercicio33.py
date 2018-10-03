for x in range(10,99):
    for y in range(10,99):
        a=str(x)
        b=str(y)
        if float(x)/y>=1:
            pass
        elif a.count("0")==1 or b.count("0")==1:
            pass
        elif b[0]==a[1] and float(y)/x==float(b[1])/int(a[0]):
            print str(x)+"/"+str(y)
            print 4*5*5