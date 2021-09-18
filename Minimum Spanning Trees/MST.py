import sys

class edges:
    
    def __init__(self,fromNode,toNode,edgeWeight):
        self.fromNode=fromNode
        self.toNode=toNode
        self.edgeWeight=edgeWeight
        
    def getFrom(self):
        return self.fromNode
    def getTo(self):
        return self.toNode
    def getWeight(self):
        return self.edgeWeight

def allEdge(G):
    E=[]
    file=open(G,"r+")
    f=file.readline()
    
    while f!="":
        f=file.readline()
        f=f.strip()
        if f!="":
            g=f.split(" ")
            a=int(g[0])
            b=int(g[1])
            c=float(g[2])
            edge=edges(a,b,c)
            E.append(edge)
            
    file.close()
    return E

def sorti(E):
    
    for i in range(len(E)):
        for j in range(len(E)-1-i):
            if E[j].getWeight()>E[j+1].getWeight():
                
                temp=E[j]
                E[j]=E[j+1]
                E[j+1]=temp
                
                temp1=E[j]
                E[j]=E[j+1]
                E[j+1]=temp1
                
                temp2=E[j]
                E[j]=E[j+1]
                E[j+1]=temp2

    return E                

def find(V,i):
    for j in range(len(V)):
        if i in V[j]:
            return V[j]

def merge(V,V1):
    v=[]
    for i in V:
        v.append(i)
        
    for i in V1:
        if i not in v:
            v.append(i)
    return v

def kruskal(G):
    
    E=allEdge(G)
    S=sorti(E)
    file=open(G,"r")
    f=int(file.readline().strip())
    
    V=[]
    for i in range(f):
        V.append([])

    for i in range(f):
        V[i].append(i)
    
    while len(V)>1 and len(S)>0:
        nextEdge=S.pop(0)
        vSet1=find(V,nextEdge.getFrom())
        vSet2=find(V,nextEdge.getTo())
        
        if vSet1!=vSet2:
            if nextEdge.getFrom()<nextEdge.getTo():
                print("Select Edge: ["+str(nextEdge.getFrom())+", "+str(nextEdge.getTo())+", "+str(nextEdge.getWeight())+"]")
            else:
                print("Select Edge: ["+str(nextEdge.getTo())+", "+str(nextEdge.getFrom())+", "+str(nextEdge.getWeight())+"]")
            V.remove(vSet1)
            V.remove(vSet2)
            merged=merge(vSet1,vSet2)
            V.append(merged)
            
def adjacency(i):
    file = open(i,"r")
    f=file.readline().strip()
    n=int(f)
    A=[]
    for i in range(n):
        A.append([])
        for j in range(n):
            A[i].append(float('inf'))
    while f!="":
        f=file.readline()
        f=f.strip()
        if f!="":
            g=f.split(" ")
        a=int(g[0])
        b=int(g[1])
        c=float(g[2])
        A[a][b]=c
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i][j]=float('inf')
    file.close()
    return A

def diff(V,U):
    v=[]
    for i in V:
        if i not in U:
            v.append(i)
    return v

def prim(G,n):
    
    file=open(G,"r")
    f=int(file.readline().strip())
    
    T=[]
    U=[n]
    V=[]
    
    m=float('inf')
    fr=0
    t=0
    
    A=adjacency(G)
    for i in range(f):
        V.append(i)
    
    c=0
    while diff(V,U)!=[]:
        different=diff(V,U)
        m=float('inf')
        
        for i in U:
            for j in different:
                if A[i][j]<m:
                    m=A[i][j]
                    t=j
                    fr=i
                    weight1=A[i][j]
                    c=1  
                if A[j][i]<m:
                    m=A[j][i]
                    t=j
                    fr=i
                    weight1=A[j][i]
                    c=2
        print("Added "+str(t))
        if t<fr:
            print("Using Edge ["+str(t)+", "+str(fr)+", "+str(weight1)+"]")
        else:
            print("Using Edge ["+str(fr)+", "+str(t)+", "+str(weight1)+"]")
        U.append(t)
        
def menu():
    print("Commands: \nexit or ctrl-d - quits the program\nhelp - prints this menu\nprim integer_value - run's Prim's algorithm starting at node given\nkruskal - runs Kruskal's algorithm")


print("Welcome to Minimum Spanning Tree Finder")
i=input("Give the file name graph is in:\n")
menu()
command=input("Enter command:\n")
while command != "exit":
    if command=="help":
        menu()
        command=input("Enter command:\n")
    elif command=="kruskal":
        print("Running Kruskal's Algorithm")
        kruskal(i)
        command=input("Enter command:\n")
    elif command[0:4]=="prim":
        print("Running Prim's Algorithm")
        print("Starting Node:",command[-1])
        prim(i,int(command[-1]))
        command=input("Enter command:\n")
    else:
        print("Unknown Command")
        command=input("Enter command:\n")
print("Bye")
sys.exit()