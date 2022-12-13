
from queue import Queue
import traversal

def searchBT(root,element):
    if not root:
        return
    q = Queue(0)
    q.put(root)

    while not q.empty():
        value = q.get(block=False)
        if value.data ==element:
            print(f"{element=} does exist!!")
            return
        if value.left:
            q.put(value.left)
        if value.right:
            q.put(value.right)
    
    print(f"{element=} does not exist!!")


searchBT(traversal.root,"Tea")
