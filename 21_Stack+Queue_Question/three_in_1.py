# Create 3 stack in one single list

from cgi import print_arguments


class Multistack:
    def __init__(self,stack_size) -> None:
        self.numstack = 3
        self.stacksize  = stack_size
        self.stack = [0] * stack_size * self.numstack
        self.sizeStack = [0]*self.numstack
    
    def __str__(self) -> str:
        print("Inside str")
        # v = [str(item) for item in self.stack]
        # return " ".join(v)
    
    def isEmpty(self,stacknum):
        if self.sizeStack[stacknum]:
            return False
        else:
            return True
    
    def isFull(self,stacknum):
        if self.sizeStack[stacknum]==self.stacksize:
            return True
        else:
            return False 
    
    def __indexOfTop(self,stacknum):
        offset = stacknum*self.stacksize
        return offset+self.sizeStack[stacknum]-1
    
    def push(self,stacknum,item):
        if self.isFull(stacknum):
            return "Stack is Full!"
        else:
            self.sizeStack[stacknum]+=1
            self.stack[self.__indexOfTop(stacknum)] = item 
            
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "Stack is Empty!"
        else:
            value = self.stack[self.__indexOfTop(stacknum)]
            self.stack[self.__indexOfTop(stacknum)] = 0
            self.sizeStack[stacknum]-=1
            return value
            
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "Stack is Empty!"
        else:
            value = self.stack[self.__indexOfTop(stacknum)]
            return value 
        
ms = Multistack(3)
ms.push(2,45)
ms.push(2,12)
ms.push(2,78)
ms.push(0,40)
ms.push(0,20)
ms.push(0,10)
print(ms)
# ms.pop(2)
# print(ms.peek(2))
# print(ms)
