class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head, k: int):
    def reverse(head, k):
        if k == 0:
            return head
        newhead = reverse(head.next, k-1)
        head.next.next = head
        head.next = None
        return newhead

    dummy = temp = ListNode(-1, head)
    future = head

    while future:
        cnt = k
        while cnt:
            if future is None:
                return dummy.next
            future = future.next
            cnt -= 1

        newhead = reverse(temp.next, k-1)
        temp.next.next = future
        temp.next = newhead

        while temp.next != future:
            temp = temp.next

    return dummy.next


k = 2
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print(reverseKGroup(head, k))
