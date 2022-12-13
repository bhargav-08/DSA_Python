import sys
sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList,Node

class Queue:
    def __init__(self) -> None:
        self.q = LinkedList()
        
    def __str__(self) -> str:
        return self.q.__str__()
    
    def isEmpty(self):
        if self.q.head == None:
            return True
        else:
            return False
    
    def enqueue(self,value):
        node = Node(value)
        if self.q.head == None:
            self.q.tail = node
            self.q.head = node
        else:
            self.q.tail.next = node
            self.q.tail = node

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty!!"
        else:
            value = self.q.head.value
            self.q.head= self.q.head.next
            return value
    
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty!!"
        else:
            value = self.q.head.value
            return value

    def delete(self):
        self.q.head = None
        self.q.tail = None
    
customQ = Queue()

customQ.enqueue(2)
customQ.enqueue(20)

customQ.enqueue(56)
# print(customQ)

customQ.dequeue()
customQ.dequeue()
customQ.dequeue()
print(customQ.dequeue())



print(customQ)