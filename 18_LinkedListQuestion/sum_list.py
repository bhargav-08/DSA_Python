
import sys
sys.path.append("C:\\Users\\HP\Desktop\\DSA_Python\\18_LinkedListQuestion")

from linkedlist import LinkedList

def sumList(ll1,ll2):
    head1 = ll1.head
    head2 = ll2.head
    
    sum = 0
    place = 0
    answer = LinkedList()
    while head1:
        sum=sum+(head1.value+head2.value)*pow(10,place)
        place+=1 
        head1=head1.next;head2=head2.next;

    for i in str(sum)[::-1]:
        answer.add(i)
    return answer


def otherMethod(ll1,ll2):
    head1 = ll1.head
    head2 = ll2.head
    sum = LinkedList()
    carry = 0
    
    while head1 or head2:
        result = carry
        if head1:
            result = result+head1.value
            head1=head1.next
        if head2:
            result = result+head2.value
            head2=head2.next
        carry = result//10
        sum.add(result%10)
        
    if carry:
        sum.add(carry)
    return sum
    
ll1 = LinkedList()
ll2 = LinkedList()
ll1.generateLL(3,0,9)
ll2.generateLL(3,0,9)
print(ll1)
print(ll2)

# answer = sumList(ll1,ll2)
answer = otherMethod(ll1,ll2)
print(answer)
# print(ll)