from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
print("Dequeue is "+ str(q.popleft()))
q.clear()
q.append(4)

print(q)

"""
=> Methods of collections.deque
deque() - create a Queue
append() - just like enqueue
popleft() - just like dequeue
clear() - delete the queue

* IMP - After adding element more than its size will override its front element
"""
