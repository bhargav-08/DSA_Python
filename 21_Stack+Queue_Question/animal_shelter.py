class AnimalShelter:
    def __init__(self) -> None:
        self.list = []
        
    def enqueue(self,item):
        return self.list.append(item)
        
    def dequeueAny(self):
        if len(self.list):
            return self.list.pop(0)
        return None
        
    def dequeueDog(self):
        value = None
        for item in self.list:
            if item.startswith("dog"):
                value = self.list.index(item)
                break
        if value==None:
            return None        
        return self.list.pop(value)

    def dequeueCat(self):
        value = None
        for item in self.list:
            if item.startswith("cat"):
                value = self.list.index(item)
                break
            
        if value==None:
            return None
        return self.list.pop(value)
    
    def __str__(self) -> str:
        values = [item for item in self.list]
        return ":".join(values)
    
a_s = AnimalShelter()
a_s.enqueue("dog1")
a_s.enqueue("dog2")
a_s.enqueue("cat1")
a_s.enqueue("dog3")
# print(a_s.dequeueAny())
# print(a_s.dequeueCat())
# print(a_s.dequeueCat())
print(a_s.dequeueDog())
print(a_s.dequeueDog())
print(a_s.dequeueDog())
print(a_s.dequeueDog())
print(a_s.dequeueAny())
print(a_s.dequeueAny())
        