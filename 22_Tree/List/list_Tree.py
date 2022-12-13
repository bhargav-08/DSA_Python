class BTList:
    def __init__(self,size) -> None:
        self.maxsize = size
        self.list = size * [None] 
        self.lastIndex = 0
        
        
    def insertNode(self,item):
        if self.lastIndex+1==self.maxsize:
            return "Tree is Full!!"
        else:
            self.lastIndex+=1
            self.list[self.lastIndex] = item
            return "Element inserted Successfully!!"
        
        
    def searchNode(self,item):
        for i in range(len(self.list)):
            if self.list[i]==item:
                return "Element is Present!!"
        return "Element is not Present 😒🙁"
    
    
    def preOrder(self,index=1):
        if index > self.lastIndex:
            return 
        print(self.list[index])
        self.preOrder(index*2)
        self.preOrder(index*2+1)
        
        
    def inOrder(self,index=1):
        if index > self.lastIndex:
            return 
        self.inOrder(index*2)
        print(self.list[index])
        self.inOrder(index*2+1)
        
        
    def postOrder(self,index=1):
        if index > self.lastIndex:
            return 
        self.postOrder(index*2) # left
        self.postOrder(index*2+1) # right
        print(self.list[index]) # root
        
    def levelOrder(self,index=1):
        for i in range(index,self.lastIndex+1):
            print(self.list[i])
            
    def deleteNode(self,value):
        if self.lastIndex==0:
            return "Binary Tree is Empty!!"

        for i in range(1,self.lastIndex+1):
            if self.list[i]==value:
                self.list[i] = self.list[self.lastIndex]
                self.list[self.lastIndex] = None
                self.lastIndex-=1
                return "Node deleted Successfully"
        
        return "No such element found!!"
    
    
    def deleteEntireTree(self):
        self.list = None
        return "Successfully Deleted Binary Tree!!"
bt = BTList(8)
bt.insertNode("Drinks")
bt.insertNode("Hot")
bt.insertNode("Cold")
bt.insertNode("Tea")
bt.insertNode("Coffee")
# print(bt.searchNode(30))
# bt.preOrder(1)
# bt.inOrder(1)  # left root right
# bt.postOrder(1)  # left(2*index) right(2*index+1) root
# bt.levelOrder(1)
# print(bt.deleteNode("Coffee"))
# print(bt.deleteEntireTree())
# print()
bt.levelOrder(1) 
# bt.inOrder()