
class LinkedList:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def add(self,node):
        self.next = node

    def __str__(self) -> str:
        head = self
        values = ""
        while head:
            values = values + " "+ str(head.data)
            head=head.next
        # print("VAlues are" ,values)
        return values

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

def depth(root):
    # if not root:
    #     return 0

    if root.right==None and root.left is None:
        return 1

    left = depth(root.left) +1
    right = depth(root.left) +1
    return max(left,right)

def treeToLL(root,customdict={}):
    if root is None:
        return

    d = depth(root)

    if customdict.get(d)==None:
        customdict[d] = LinkedList(root.data)
    else:
        head = customdict[d]
        while head.next:
            head=head.next
        head.add(LinkedList(root.data))

    treeToLL(root.left)
    treeToLL(root.right)
    return customdict

root = Node(1)
two = Node(2)
three  = Node(3)
four  = Node(4)
five = Node(5)
six  = Node(6)
seven = Node(7)

root.right = three
root.left = two
two.right = five
two.left = four
three.right = seven
three.left = six

customdict = treeToLL(root)
# print(customdict)
for k,v in customdict.items():
    print("Values at level -" ,v)