import sys
import math

def help():
    print("Possible Commands are: \ndijkstra x - Runs Dijkstra starting at node X. X must be an integer\nfloyd - Runs Floyd's algorithm\nhelp - prints this menu\nexit or ctrl-D - Exits the program")

def adjacency():
    file = open(file1,"r")
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
                A[i][j]=float(0)
    file.close()
    return A
    
def floyd(G):
    file = open(file1,"r")
    f=file.readline().strip()
    n=int(f)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0, n):
                if G[i][k]+G[k][j]<G[i][j]:
                        G[i][j]=float(G[i][k]+G[k][j])
    file.close()
    return G
    
def dijkstra(G,z):
    class heap:
        def __init__(self):
            self.data=[]
        def empty(self):
            return len(self.data)==0
        def insert(self,x):
            self.data.append(x)
            self.upheap(len(self.data)-1)
        def parent(self,index):
            return math.floor((index - 1) / 2)
        def left(self,index):
            return ( index + 1 ) * 2 - 1
        def right(self,index):
            return ( index + 1 ) * 2
        def swap(self,a,b):
            temp = self.data[a]
            self.data[a] = self.data[b]
            self.data[b] = temp
        def upheap(self , index):
            if self.parent(index) < 0:
                return 0
            p = self.data[self.parent(index)]
            if p <= self.data[index]:
                return 0
            self.swap(index , self.parent(index))
            self.upheap(self.parent(index))
        def min(self):
            m = self.data[0]
            for i in range(0, len(self.data)):
                if self.data[i] < m:
                    m = self.data[i]
            return m
        def deletemin(self):
            temp = self.min()
            self.swap(self.data.index(temp) , len(self.data) - 1)
            self.data.pop(self.data.index(self.min()))
            self.downheap(0)
        def downheap(self , index):
            if self.left(index) >= len(self.data) or self.right(index) >= len(self.data):
                return 0
            if self.data[self.left(index)] == None and self.data[self.right(index)] == None:
                return 0
            if self.data[index] <= self.data[self.right(index)]  and self.data[index] <= self.data[self.left(index)]:
                return 0
            if self.data[self.left(index)] <= self.data[self.right(index)]:
                self.swap(index , self.left(index))
                self.downheap(self.left(index))
            else:
                self.swap(index , self.right(index))
                self.downheap(self.right(index))
        
    s={z}
    d=[]
    for i in range(0,len(G)):
        d.append(float('inf'))
    d[z]=0.0
    Q=heap()
    for i in range(0,len(G)):
        Q.insert(i)
    
    while not Q.empty():
        u=Q.min()
        Q.deletemin()
        s.add(u)
        for i in range(0,len(G)):
            if d[i]>d[u]+G[u][i]:
                d[i]=float(d[u]+G[u][i])
    
    return d 
   
file1=input("File containing graph:\n")
help()
command=input("Enter command:\n")

while command!="exit":
    if command=="help":
        help()
        command=input("Enter command:\n")
    if command=="floyd":
        G=adjacency()
        f=floyd(G)
        for i in f:
            print(i)
        command=input("Enter command:\n")
    if command[0:8]=='dijkstra':
        A=adjacency()
        floyd(A)
        start=int(command[-1])
        print(dijkstra(A,start))
        command=input("Enter command:\n")
            
print("Bye")
sys.exit()