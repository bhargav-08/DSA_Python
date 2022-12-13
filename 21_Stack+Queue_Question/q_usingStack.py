class Stack:
    def __init__(self) -> None:
        self.list = []
        
    def __len__(self):
        return len(self.list)
    
class Queue:
    def __init__(self) -> None:
        self.s1  = Stack()
        self.s2  = Stack()
        
    def __str__(self) -> str:
        values = [str(item) for item in self.s1.list]
        return " ".join(values)

    def enqueue(self,item):
        self.s1.list.append(item)
        
    def dequeue(self):
        while len(self.s1):
            value = self.s1.list.pop()
            self.s2.list.append(value)
        
        item = self.s2.list.pop()

        while len(self.s2):
            value = self.s2.list.pop()
            self.s1.list.append(value)
        
        return item

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.dequeue()
print(q) 