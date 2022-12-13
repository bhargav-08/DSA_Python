
class Queue:
    def __init__(self) -> None:
        self.list = []
        
    def __str__(self) -> str:
        e = [str(element)for element in self.list]
        return " ".join(e)

    def isEmpty(self):
        return True if self.list==[] else False
    
    def enqueue(self,value):
        self.list.append(value)
        return "Added Element Successfully"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty!!"
        else:
            value =self.list.pop(0)
            return value
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty!!"
        else:
            return self.list.__getitem__(0)
        
q = Queue() 
q.enqueue(10)
q.enqueue(23)
q.enqueue(67)
q.enqueue(58)
print(q)
q.dequeue()
q.enqueue(59)
print(q.peek())

print(q)

