from collections import defaultdict


class Allocator:

    def __init__(self, n: int):
        self.memory = [0 for _ in range(n)]
        self.loc = defaultdict(list)  # mid:[(s,e),(s,e)]
        self.free = n

    def allocate(self, size: int, mID: int) -> int:
        if self.free < size or self.free == 0:
            return -1

        i = 0
        start = i
        c = 0
        while i < len(self.memory):
            if self.memory[i] == 0:
                c += 1
                if size == c:
                    # total size is available
                    self.memory[start:start+size] = mID
                    self.free = self.free-size
                    self.loc[mId].append((start, start+size))
                    return start
            else:
                c = 0
                start = i+1
            i += 1

    def free(self, mID: int) -> int:
        total = 0
        for mIDs in self.loc:
            for s, e in mIDs:
                self.memory[s:e] = 0
                self.free += e-s
                total = total + e-s
        return total


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size, mID)
# param_2 = obj.free(mID)


att = ["Allocator", "allocate", "allocate", "allocate", "free",
       "allocate", "allocate", "allocate", "free", "allocate", "free"]
val = [[10], [1, 1], [1, 2], [1, 3], [2], [
    3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]


grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

