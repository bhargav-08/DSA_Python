import sys

sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList,Node

def findIntersection(ll1,ll2):
    head1 = ll1.head
    head2 = ll2.head
    
    len1=len(ll1)
    len2=len(ll2)

    # print(len1,len2)
    difference = len1-len2
    
    if difference>0:
        while difference >0:
            head2=head2.next
            difference-=1
    else:
        while difference<0:
            head1=head1.next
            difference+=1
    while head1 or head2:
        if head1==head2:
            return head1
        head1=head1.next;head2=head2.next
    return "Both linked List have no intersection!!"

def addSameNode(ll1,ll2,value):
    temp = Node(value)
    ll1.tail.next = temp
    ll1.tail= temp
    ll2.tail.next = temp
    ll2.tail= temp
    
    

ll1 = LinkedList()
ll2 = LinkedList()
ll1.generateLL(10,1,100)
ll2.generateLL(10,1,100)

addSameNode(ll1,ll2,14)
addSameNode(ll1,ll2,3)
addSameNode(ll1,ll2,27)
print(findIntersection(ll1,ll2))
