encontrado=0
contador=1
tracker=[]
instancias=[]

class Node:
    def __init__ (self, x):
        self.name=x
        self.parent = x
        self.size=1
    def changevalue(self,x,y):
        if y==1:
            self.parent=x
        else:
            self.size+=x

def Union(x, y):
    xRoot = Find(instancias[x-1])
    yRoot = Find(instancias[y-1])
    if xRoot==yRoot:
        return
    if instancias[xRoot-1].size < instancias[yRoot-1].size:
        instancias[yRoot-1].changevalue(instancias[xRoot-1].size,2)
        instancias[xRoot-1].changevalue(yRoot,1)
    elif instancias[xRoot-1].size >= instancias[yRoot-1].size:
        instancias[xRoot-1].changevalue(instancias[yRoot-1].size,2)
        instancias[yRoot-1].changevalue(xRoot,1)
        

def Find(x):
    if x.parent != x.name:
        x.parent = Find(instancias[x.parent-1])
    return x.parent

def callGenerator(contador):
    llamador=2*contador-1
    llamado=2*contador
    global tracker
    if llamador<=55:
        llamador=(100003 - 200003*llamador + 300007*llamador*llamador*llamador)%1000000
        tracker.append(llamador)
    else:
        llamador=(tracker[0]+tracker[31])%1000000
        tracker.append(llamador)
        tracker.remove(tracker[0])
        
    if llamado<=55:
        llamado=(100003 - 200003*llamado + 300007*llamado*llamado*llamado)%1000000
        tracker.append(llamado)
    else:
        llamado=(tracker[0]+tracker[31])%1000000
        tracker.append(llamado)
        tracker.remove(tracker[0])    
    return llamador, llamado

#creamos los nodos
for x in range(1,1000001):
    a=Node(x)
    instancias.append(a)
    
sumatotal=0

while instancias[Find(instancias[524287-1])-1].size<990000:
    a=callGenerator(contador)
    if a[0]!=a[1]:
        sumatotal+=1
        Union(a[0],a[1])
    contador+=1
    
print (sumatotal)