from sLinkedList import SLinkedList, Node


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLL(start, end):
    if start == end or start.next is None:
        return end
    newhead = reverseLL(start.next, end)
    nexthead = start.next
    nexthead.next = start
    start.next = None
    return newhead


def reverseKGroup(head, k: int):
    if head is None or k == 1 or head.next is None:
        return head
    s = head
    e = head
    inc = k-1
    while inc:
        if e.next is None:
            return s
        e = e.next
        inc -= 1
    reversedHead = reverseKGroup(e.next, k)
    newhead = reverseLL(s, e)

    s.next = reversedHead
    return newhead


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

head = reverseKGroup(head, 2)

while head:
    print(head.val, end=" ")
    head = head.next
print()
