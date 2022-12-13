from multiprocessing import Queue

q = Queue(maxsize=3)

q.put(2)
q.put(3)
q.put(4)

print(q)

"""
All methods of queue.Queue except join() and taskdone()
"""