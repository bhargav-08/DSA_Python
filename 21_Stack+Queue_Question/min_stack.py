
class Node:
    def __init__(self,value,next) -> None:
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        string = str(self.value)
        if self.next:
            string+=',' + str(self.next)
        return string
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None
    
    def __iter__(self):
        temp= self.top
        while temp:
            yield temp 
            temp=temp.next
            
    def __str__(self) -> str:
        values = [str(element.value) for element in self]
        return " ".join(values)
            
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    def push(self,num):
        if self.minNode and (self.minNode.value < num) :
            self.minNode = Node(value=self.minNode.value,next=self.minNode)
        else:
            self.minNode = Node(value=num,next=self.minNode)
        self.top = Node(value=num,next=self.top)
        
    def pop(self):
        if not self.top:
            return None
        else:
            val = self.top.value
            self.top = self.top.next
            self.minNode = self.minNode.next
            return val
    
customStack = Stack()
customStack.push(23)
customStack.push(3)
customStack.push(79)
customStack.push(5)
customStack.pop()
# customStack.pop()
# customStack.pop()
# print(customStack)
# print(customStack.min())
print(customStack.min())