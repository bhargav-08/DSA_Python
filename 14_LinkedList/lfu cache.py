from collections import defaultdict


class Node:
    def __init__(self, value=-1, prev=None, next=None):
        self.val = value
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}

    def __len__(self):
        return len(self.mp)

    def pushRight(self, val):
        node = Node(val, self.tail.prev, self.tail)
        self.mp[val] = node
        self.tail.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.mp:
            node = self.mp[val]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.mp[val]
            return node

    def popleft(self):
        res = self.head.next.val
        self.pop(self.head.next.val)
        return res


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = {}  # Map key-value
        self.countMap = defaultdict(int)  # key-count
        self.listMap = defaultdict(LinkedList)  # Map count- linkedlist
        self.lfucnt = 0

    def counter(self, key):
        val = self.countMap[key]
        self.listMap[val].pop(key)
        self.countMap[key] += 1
        self.listMap[val+1].pushRight(key)

        if val == self.lfucnt and len(self.listMap[val]) == 0:
            self.lfucnt += 1

    def get(self, key: int) -> int:
        if key in self.valMap:
            self.counter(key)
            return self.valMap[key]

        return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.valMap and len(self.valMap) == self.cap:
            val = self.listMap[self.lfucnt].popleft()
            self.valMap.pop(val)
            self.countMap.pop(val)

        self.valMap[key] = value
        self.counter(key)
        self.lfucnt = min(self.lfucnt, self.countMap[key])


obj = LFUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.get(3))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(3))
