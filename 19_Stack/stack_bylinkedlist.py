import sys
sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList,Node

class Stack:
    def __init__(self) -> None:
        self.stack = LinkedList()
    
            
    def __str__(self) -> str:
        s = [str(node.value) for node in self.stack]
        return "\n".join(s)

        
    def isEmpty(self):
        if self.stack.head is None:
            return True
        else:
            return False
    
    def push(self,value):
        node = Node(value)
        node.next = self.stack.head
        self.stack.head = node
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            value = self.stack.head.value
            self.stack.head = self.stack.head.next
            return value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            return self.stack.head.value
    
    def delete(self):
        self.stack.head = None
        print("Stack deleted Successfully")
    
s = Stack()
s.push(2)
s.push(23)
s.push(45)
s.pop()
s.pop()
s.pop()

# print(s.isEmpty())
# s.push(78)
# print(s.peek())
# s.delete()
print(s)
