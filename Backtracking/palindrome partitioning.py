from functools import lru_cache


def minCut(s: str) -> int:

    @lru_cache
    def rev(s):
        return s == s[::-1]

    def bk(index):
        result = float("inf")
        if index == len(s):
            return 0
        for i in range(index, len(s)):
            if rev(s[index:i+1]):
                val = 1 + bk(i+1)
                result = min(result, val)

        return result

    return bk(0) - 1


print(minCut("aabb"))
