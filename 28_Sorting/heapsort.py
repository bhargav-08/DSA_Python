

class Heap:
    def __init__(self,size) -> None:
        self.list = [None] *(size+1)
        self.heapsize = 0
        self.maxsize = size
        self.arr = []

    def isFull(self):
        if self.heapsize==self.maxsize:
            return True
        else:
            return False

    def __str__(self) -> str:
        for i in range(1,self.heapsize+1):
            print(self.list[i],end=" ")
        return ""

    def heapifyInsert(self,index):

        if index <=1:
            return

        parent = index//2

        if self.list[parent] > self.list[index]:
            self.list[parent],self.list[index]=self.list[index],self.list[parent]
            self.heapifyInsert(parent)


    def insert(self,value):
        if self.isFull():
            print("Heap Tree is Full")
            return

        self.heapsize+=1
        self.list[self.heapsize] = value
        self.heapifyInsert(self.heapsize)

    def heapifyTop(self,index):
        left = index*2
        right =  index*2+1
        min = 0
        if left > self.heapsize:
            return

        if left==self.heapsize:
            if self.list[left] < self.list[index]:
                self.list[left],self.list[index]= self.list[index],self.list[left]
                self.heapifyTop(left)

        else:
            if self.list[left] > self.list[right]:
                min=right
            else:
                min=left

            if self.list[min] < self.list[index]:
                self.list[min],self.list[index]=self.list[index],self.list[min]
                self.heapifyTop(min)


    def extractTop(self):
        if self.heapsize==0:
            print("Heap Tree is Empty! ")
            return
        self.arr.append(self.list[1])
        self.list[1] = self.list[self.heapsize]
        self.list[self.heapsize] = None
        self.heapsize-=1
        self.heapifyTop(1)

    def minarr(self):
        while self.heapsize > 0:
            self.extractTop()
        return self.arr

root = Heap(10)
root.insert(10)
root.insert(5)
root.insert(22)
root.insert(67)
root.insert(39)
root.insert(100)
root.insert(1)
root.insert(78)
root.insert(56)
root.insert(39)
# print(root)
print(root.minarr())