
class CircularQueue:
    def __init__(self,size) -> None:
        self.list = size*[None]
        self.maxsize = size
        self.front = -1
        self.rear = -1
        
    def __str__(self) -> str:
        values = [str(element) for element in self.list if element is not None]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.front==-1:
            return True
        else:
            return False
        
    def isFull(self):
        if (self.rear+1)%self.maxsize==self.front:
            return True
        else:
            return False
    
    def enqueue(self,value):
        if self.isFull():
            print("Circular Queue is Full!")
            return
        else:
            if self.front==-1:
                self.front=0
                self.rear=0
                self.list[self.front] = value
            else:
                self.rear=(self.rear+1)%self.maxsize
                self.list[self.rear]=value
            
    def dequeue(self):
        if self.isEmpty():
            return "Ciricular Queue is Empty!"
        else:
            if self.front==self.rear:
                value = self.list[self.front]
                self.list[self.front]  = None
                self.front=-1
                self.rear=-1
            else:
                value = self.list[self.front]
                self.list[self.front]  = None
                self.front=(self.front+1)%self.maxsize
            return value
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty!!"
        else:
            return self.list[self.front]
        
    def delete(self):
        self.list = self.maxsize*[None]
        self.front = -1
        self.rear= -1
        
cq = CircularQueue(4)    
cq.enqueue(23)
cq.enqueue(18)
cq.enqueue(34)
cq.enqueue(95)
# print(cq.dequeue())
print(cq.peek())
print(cq)
        