
class Stack:
    def __init__(self,size) -> None:
        self.list = []
        self.maxsize = size
    
    def __str__(self) -> str:
        self.list.reverse()
        stack = [str(element) for element in self.list]
        return "\n".join(stack)
    
    def isEmpty(self) -> bool:
        if self.list ==[]:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if len(self.list) ==self.maxsize:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            return "Linked List is Full!!"
        else:
            self.list.append(value)
            return "Successfully pushed the element in Stack"

    def pop(self) -> int| str:
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            return self.list.pop()
        
    def peek(self) -> int | str:
        if self.isEmpty():
            return "Stack is Empty!!"
        else:
            return self.list[len(self.list)-1]
        
    def deleteStack(self):
        self.list = None
        
customStack = Stack(4)
# print(customStack.isEmpty())
customStack.push(23)
customStack.push(34)
customStack.push(19)
customStack.push(29)
print(customStack.isFull())

# print(customStack.peek())
print(customStack.pop())
print(customStack)

