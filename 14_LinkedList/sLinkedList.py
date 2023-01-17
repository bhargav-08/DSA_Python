# Creating Singly Linked List

class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __str__(self) -> str:

        return " ".join([str(node.value) for node in self])

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.next

    def insertLL(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == 1:
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                if tempNode is None:
                    raise Exception("Enter Proper Index!!")

                newNode.next = tempNode.next
                tempNode.next = newNode

                if newNode.next is None:
                    self.tail = newNode

    def traversal(self):
        if self.head is None:
            return "Linked List is Empty"
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def search(self, element):
        if self.head is None:
            return "Linked List is Empty"
        else:
            temp = self.head
            while temp is not None:
                if temp.value == element:
                    return temp.value

                temp = temp.next

            return ("Element not Found")

    def delete(self, location):
        if self.head is None:
            return "Linked List is Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                index = 0
                temp = self.head
                while index < location-1:
                    temp = temp.next
                    index += 1
                nextNode = temp.next
                temp.next = nextNode.next

    def deleteEntire(self):
        if self.head is None:
            print("Linked List is Empty!!")
        else:
            self.head = None
            self.tail = None


if __name__ == "__main__":
    firstList = SLinkedList()
    firstList.insertLL(1, 1)
    firstList.insertLL(2, 1)
    firstList.insertLL(3, 1)
    firstList.insertLL(4, 1)
    firstList.insertLL(0, 0)
    firstList.insertLL(10, 5)

    print([node.value for node in firstList])
    # firstList.delete(1)
    firstList.deleteEntire()

    print([node.value for node in firstList])

    # print(firstList.search(10))
    # print(firstList.search(100))
    # print([node.value for node in firstList])
    # firstList.traversal()
