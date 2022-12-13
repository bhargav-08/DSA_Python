import sys
import os
sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList


ll = LinkedList()
ll.generateLL(10,1,100)
print(ll)
ll.removeDuplicate()
print(ll)
