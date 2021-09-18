class Node:
    
    def __init__(self , value , valueRight = None , valueLeft = None):
        
        self.value = value
        self.valueRight = valueRight
        self.valueLeft = valueLeft
    
    def setRight(self , value):
        
        self.valueRight = value
    
    def setLeft(self , value):
        
        self.valueLeft = value
    
    def getRight(self):
        
        return self.valueRight
    
    def getLeft(self):
        
        return self.valueLeft
        
    def getValue(self):
        
        return self.value  
    
class BST:
    def __init__(self):
        
        self.node = None
        self.order = ""
        
    def __str__(self):
        
        if self.node is None:
            
            return "Empty Tree"
            
        else:
            
            self.order += "Preorder: " 
            self.pre(self.node)
            self.order += "\n" 
            
            self.order += "Inorder: " 
            self.ino(self.node)
            self.order += "\n" 
            
            self.order += "Postorder: " 
            self.post(self.node)
            
            
            return self.order
    
    def pre(self , treeNode):
        
        if treeNode is not None:
            
            self.order += str(treeNode.getValue()) + " "
            self.pre(treeNode.getLeft())
            self.pre(treeNode.getRight())
            
        else:
            
            self.order += "N "
    
    def ino(self , treeNode):
        
        if treeNode is not None:
            
            self.ino(treeNode.getLeft())
            self.order += str(treeNode.getValue()) + " "
            self.ino(treeNode.getRight())
            
        else:
            
            self.order += "N "
    
    def post(self , treeNode):
        
        if treeNode is not None:
            
            self.post(treeNode.getLeft())
            self.post(treeNode.getRight())
            self.order += str(treeNode.getValue()) + " "
            
        else:
            
            self.order += "N "
            
            
    def insert(self , x):
        
        newNode = Node(x)
        rootNode = self.node
        
        if rootNode is None:
            
            self.node = Node(x)
            return 0
        
        while rootNode is not None:
            
            if rootNode.getValue() < x:
                
                if rootNode.getRight() == None:
                    
                    rootNode.setRight(newNode)
                    return 0
                
                else:
                    
                    rootNode = rootNode.getRight()
                    
            if rootNode.getValue() > x:
                
                if rootNode.getLeft() == None:
                    
                    rootNode.setLeft(newNode)
                    return 0
                
                else:
                    
                    rootNode = rootNode.getLeft()
            
            if rootNode.getValue() == x:
                
                return 0
        
    def find(self,x):
        
        found = True
        
        if self.node == None:
            
            return not found
        
        rootNode = self.node
        
        while rootNode is not None:
            
            if rootNode.getValue() < x :
                
                rootNode = rootNode.getRight()
            
            elif rootNode.getValue() > x :
                
                rootNode = rootNode.getLeft()
                
            else:
            
                return found
        
        return not found

        
