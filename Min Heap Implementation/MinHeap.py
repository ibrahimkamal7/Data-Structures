import math
class heap:
    def __init__(self):
        
        self.data = []
        
        self.string = "" 
        self.string1 = ""
        self.string2 = ""
        
    def __str__(self):
        
        res = ""
        
        for x in self.data:
            res=res + str(x) + " "
            
        return res
        
    def makenull(self):
        
        self.data.clear()
        
    def insert(self , x):
        
        self.data.append(x)
        self.upheap(len(self.data) - 1)
    
    def parent(self , index):
        
        return math.floor((index - 1) / 2)
        
    def left(self , index):
        
        return ( index + 1 ) * 2 - 1
        
    def right(self,index):
        
        return ( index + 1 ) * 2
        
    def swap(self , a , b):
        
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

    def inorder(self , index):
        
        self.string =""
        
        if index >= len(self.data):
            return ""
        
        else:
            
            self.string += str(self.inorder(self.left(index)))
            self.string += str(self.data[index]) + " "
            self.string += str(self.inorder(self.right(index)))
        
        return self.string
        
        
    def preorder(self , index):
        
        self.string1 = ""
        
        if index >= len(self.data):
            return ""
       
        else:
            
            self.string1 += str(self.data[index]) + " "
            self.string1 += str(self.preorder(self.left(index)))
            self.string1 += str(self.preorder(self.right(index)))
       
        return self.string1
            
            
    def postorder(self , index):
        
        self.string2 = ""
        
        if index >= len(self.data):
            return ""
        
        else:
            
            self.string2 += str(self.postorder(self.left(index)))
            self.string2 += str(self.postorder(self.right(index)))
            self.string2 += str(self.data[index]) + " "
        
        return self.string2
        
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
        
        return temp
        
        
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
        
    def sort(self):
        
        for i in range(len(self.data)):
            print(self.deletemin())