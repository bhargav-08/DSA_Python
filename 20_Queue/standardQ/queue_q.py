from queue import Queue

q = Queue(maxsize=0)
print(q.empty())
q.put(1)
q.put(2)

print(q.qsize())
print(q.full())
print(q.get())
print(q.get())
print(q.get(block=False))
print(q)

"""
This is used for multi-producer and multi-consumer  for threading
Queue method -
1. Queue() -  create queue
2. put() - like enqueue
3. get() - like dequeue
4. qsize() - get size
5. empty() - will empty the queue 
"""