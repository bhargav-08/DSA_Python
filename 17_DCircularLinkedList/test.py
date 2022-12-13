# create , insert,traversal,reverse traversal,serach , delete, deleteEntire
from locale import currency
import random
from re import L
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next= None
        
class DCLList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            if temp==self.tail:
                break
            temp=temp.next
            
    def __str__(self) -> str:
        value = [str(item.data) for item in self]
        return '->'.join(value) 
    
    def insert(self,value,index):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            self.head.next = node
            
        else:
            if index==0:
                if self.head==self.tail:
                    self.head.next = node
                    node.next = self.head
                    self.tail = self.head
                    self.head.prev = node 
                    self.head = node
                else:
                    node.next = self.head
                    self.head  = node
                    self.tail.next = node
                    
            elif index==1:
                if self.head==self.tail:
                    self.head.next = node
                    self.tail = node
                    self.tail.prev = self.head
                    self.tail.next = self.head
                else:
                    self.tail.next = node
                    node.prev = self.tail
                    node.next = self.head
                    self.tail = node    
            else:
                location = 0
                temp = self.head
                while location <index-1 :
                    temp = temp.next
                    location+=1
                    
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
                node.prev = temp
    
    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            if temp==self.tail:
                break
            temp=temp.next
            
    def rtraversal(self):
        temp = self.tail
        while temp:
            print(temp.data,end=" ")
            if temp==self.head:
                break
            temp=temp.prev
            
    def delete(self,index):
        if self.head is None:
            return "Linked List is Empty!!"
        else:
            if index==0:
                if self.head==self.tail:
                    self.head = None
                    self.tail.next = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif index==1:
                if self.head==self.tail:
                    self.head = None
                    self.tail.next = None
                    self.tail = None
                else:
                    self.tail =self.tail.prev
                    self.tail.next =self.head
            else:
                temp =self.head
                location = 0
                while  location < index-1:
                    temp = temp.next
                    location+=1
                temp.next = temp.next.next
                temp.next.prev = temp
        
    def removeDuplicate(self):
        visited  = set()
        current = self.head
        visited.add(current.data)
        while current!=self.tail:
            if current.next.data in visited:
                if current.next==self.tail:
                    current.next = self.head
                    self.tail=current
                    break
                current.next = current.next.next
                current.next.prev = current
                continue
            else:
                visited.add(current.next.data)
            current=current.next
                
    def llgenerate(self,start,end,quantity):
        for i in range(quantity):
            
            self.insert(random.randint(start,end),0)
            
    def partition(self,value):
        temp = self.head
        
        while temp:
            if temp.next.data < value:
                self.insert(temp.next.data,0)
                if temp.next==self.tail:
                    temp.next=self.head
                    self.tail=temp
                    break                
                temp.next =temp.next.next
                temp.next.prev= temp
                continue
            if temp.next==self.tail:
                break
                
            temp=temp.next
    
    def partit(self,x):
        curNode = self.head
        end = self.tail
        self.tail = self.head
        
        while curNode:
            nextNode = curNode.next
            curNode.next = None
            if curNode.data < x:
                curNode.next = self.head
                self.head = curNode
            else:
                self.tail.next = curNode
                self.tail =curNode
            if curNode==end:
                break
            curNode=nextNode
        if self.tail.next is not None:
            self.tail.next = None
      
dcll = DCLList()
dcll.llgenerate(1,100,10)

print(dcll)
# dcll.delete(3)
# print(dcll)
# dcll.removeDuplicate()
# dcll.partition(50)
dcll.partit(50)
print(dcll)
# dcll.par


                
                
                    
            

        