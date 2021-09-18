class Node:
    def __init__(self,value,next = None):
        
        self.__value = value
        self.__next = next
        
    def __str__(self):
        
        return "[ "+str(self.__value)+" ]"
        
    def getNext(self):
        
        return self.__next
        
    def setNext(self,n):
        
        self.__next = n
        
    def getValue(self):
        
        return self.__value
        
    def setValue(self,v):
        
        self.__value = v

class Queue:
    def __init__(self):
        
       self.queue = None
       
    def __str__(self):
        
        if self.queue == None:
            return "Queue Empty"
            
        else:
            head = self.queue
            items = ""
            while head != None:
                items = items + str(head) 
                head = head.getNext()
            return items
            
    def front(self):
        
        head = self.queue
        return head.getValue()
        
    def empty(self):
        
        return self.queue == None
        
    def enqueue(self,x):
        
        newItem = Node(x)
        
        if self.queue == None:
            self.queue = newItem
        else:
            head = self.queue
            while head.getNext() != None:
                head = head.getNext()
            head.setNext(newItem)
            
    def dequeue(self):
        
        head = self.queue
        self.queue = head.getNext()
        
def main():
    print("The Josephus Problem")
    
    Q = Queue()
    R = Queue()
    
    N = int(input("Enter the Number of People in the Group:\n"))
    M = int(input("Enter value for Mth Person to be killed:\n"))
    
    print("Order in which people are killed:")
    
    items=""
    
    for i in range(0 , N):
        Q.enqueue(i)
   
    while not Q.empty():
        
        for i in range(1 , M):
            t = Q.front()
            Q.dequeue()
            Q.enqueue(t)
            
        R.enqueue(Q.front())
        Q.dequeue()
    
    while not R.empty():
        items = items + str(R.front()) + " "
        R.dequeue()
    
    print(items.strip())
    
main()