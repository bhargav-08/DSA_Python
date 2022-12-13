
class Node:
    def __init__(self,value,next=None) -> None:
        self.data = value
        self.next = next
        
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.data
    
    
    def __iter__(self):
        current = self.top
        while current:
            yield current
            current=current.next
            
    def __str__(self) -> str:
        values = [str(item.data) for item in self]
        return "->".join(values)
    
    def push(self,value):
        node = Node(value)
        if self.minNode and value > self.minNode.data:
            node.next = self.top
            self.top = node
            self.minNode = Node(self.minNode.data,self.minNode)
          
        else:
            node.next = self.top
            self.top = node
            self.minNode = Node(value,self.minNode)
            
            
    def pop(self):
        if self.top is None:
            return"Linked list is Empty!!"
        self.minNode =self.minNode.next
        item = self.top.data 
        self.top =self.top.next
        return item
    
st= Stack()
st.push(100)
st.push(20)
st.push(30)
st.push(40)
print(st.pop())
# print(st.pop())
print(st.min())
print(st)