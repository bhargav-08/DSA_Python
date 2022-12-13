from random import randint

class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None
        self.prev= None
    
    def __str__(self) -> str:
        return f"{self.value}"
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __str__(self) -> str:
        nodes = [str(node.value) for node in self]
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __len__(self):
        index = 0
        node = self.head
        while node:
            index+=1
            node = node.next
        return index
        
    def add(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def generateLL(self,number,min_element,max_element):
        for _ in range(number):
            self.add(randint(min_element,max_element))
        return self
        
    def removeDuplicate(self):
        node = self.head
        visited = set([node.value])
        while node.next:
            if node.next.value in visited:
                node.next = node.next.next
            else:
                node = node.next

    def nthelEmentFromLast(self,n:int) -> int:
        if self.head is None:
            return "Linked List is Empty!!"
        _node = self.head
        _temp  = self.head
        while n > 0:
            _temp = _temp.next
            n-=1
        while _temp:
            _node = _node.next
            _temp = _temp.next
        return _node.value
            
    
if __name__=="__main__":
    ll = LinkedList()
    ll.generateLL(10,1,100)
    print(ll)
    print(len(ll))