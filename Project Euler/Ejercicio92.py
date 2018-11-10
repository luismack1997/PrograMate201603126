convergen1=[]
convergen89=[]
listatemporal=[]
convergen1.append(1)
convergen89.append(89)
temporal=0
temporal2=0
convergencia89=0

for x in range(1,568):
    listatemporal.append(x)
    temporal=x
    while len(listatemporal)!=0: 
        if temporal in convergen1:
            for element in listatemporal:
                if element not in convergen1:
                    convergen1.append(element)
            listatemporal=[]
        elif temporal in convergen89:
            for element in listatemporal:
                if element not in convergen89:
                    convergen89.append(element)
            listatemporal=[]
        else: 
            if temporal not in listatemporal:
                listatemporal.append(temporal)
            for character in str(temporal):
                temporal2=int(character)*int(character)+temporal2
            temporal=temporal2
            temporal2=0

for x in range(568,10000000):
    temporal=x
    for character in str(temporal):
        temporal2=int(character)*int(character)+temporal2
    temporal=temporal2
    temporal2=0
    if temporal in convergen89:
        convergencia89+=1

a=len(convergen89)+convergencia89
print a