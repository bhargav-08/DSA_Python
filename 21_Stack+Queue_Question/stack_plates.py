

class StackPlates:
    def __init__(self,capacity) -> None:
        self.stacks = []
        self.capacity = capacity
        
    def __str__(self) -> str:
        return str(self.stacks)
    
    def push(self,item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop()
            
        if len(self.stacks)==0:
            return None
        else:
            return self.stacks[-1].pop()
        
    def popAt(self,numstack):
        if numstack < len(self.stacks):
            return self.stacks[numstack].pop()
        else:
            return None
         
s = StackPlates(2)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5) 
# print(s)

# s.pop()
print(s)
print(s.popAt(2))
        