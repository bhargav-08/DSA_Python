import sys
sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList

def partition(ll,n):
    currentNode = ll.head
    ll.tail = currentNode
    
    
    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < n:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode
    
        
ll = LinkedList()
ll.generateLL(8,1,100)
print(ll)
partition(ll,50)
print(ll)

