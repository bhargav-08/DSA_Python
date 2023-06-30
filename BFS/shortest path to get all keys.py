
# def shortestPathAllKeys(grid) -> int:
#     # 1. Count the total number of keys in the grid
#     cnt_keys = 0
#     M, N = len(grid), len(grid[0])
#     for i in range(M):
#         for j in range(N):
#             if grid[i][j].islower():
#                 cnt_keys += 1
#             if grid[i][j] == '@':
#                 start = i, j

#     grid = [list(row) for row in grid]
#     res = float("inf")

#     # 2. Try all the path until all the keys are not achieved and return steps
#     def bk(i, j, keys):
#         if len(keys) == cnt_keys:
#             return 0
#         if 0 <= i < M and 0 <= j < N and grid[i][j] != '#':
#             if grid[i][j] == -1:
#                 return float("inf")
#             elif grid[i][j].isupper():
#                 if grid[i][j].lower() not in keys:
#                     return float("inf")
#             elif grid[i][j].islower():
#                 keys.add(grid[i][j])

#             steps = float("inf")
#             val = grid[i][j]
#             grid[i][j] = -1
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 steps = min(steps, 1 + bk(i + dx, j + dy, keys))
#             grid[i][j] = val
#             if val.islower():
#                 keys.remove(grid[i][j])
#             return steps
#         return float("inf")

#     val = bk(*start, set())
#     if val == float("inf"):
#         return -1
#     else:
#         return val

from collections import deque

# This is not correct
# def shortestPathAllKeys(grid) -> int:
#     # count all the keys and initial position
#     cnt_keys = 0
#     M, N = len(grid), len(grid[0])

#     for i in range(M):
#         for j in range(N):
#             if grid[i][j].islower():
#                 cnt_keys += 1
#             elif grid[i][j] == '@':
#                 start = i, j
#     grid = [list(row) for row in grid]
#     vis = set(())
#     q, steps = deque(), 0
#     inital = (*start, '')
#     q.append(inital)
#     vis.add(inital)

#     while q:

#         s = len(q)
#         for _ in range(s):
#             i, j, key = q.popleft()
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 if len(key) == cnt_keys:
#                     return steps
#                 nx, ny = i + dx, j + dy
#                 if nx < 0 or ny < 0 or nx == M or ny == N or grid[nx][ny] == '#':
#                     continue
#                 if grid[nx][ny].islower():
#                     key = key + grid[nx][ny]
#                 if grid[nx][ny].isupper() and grid[nx][ny] not in key:
#                     continue
#                 if (nx, ny, key) in vis:
#                     continue
#                 state = nx, ny, key
#                 q.append(state)
#                 vis.add(state)

#         steps += 1

#     return steps


def shortestPathAllKeys(grid) -> int:
    # count all the keys and initial position
    m, n = len(grid), len(grid[0])

    ii = jj = total = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                ii, jj = i, j
            elif grid[i][j].islower():
                total += 1

    ans = 0
    seen = {(ii, jj, 0)}
    queue = [(ii, jj, 0)]
    while queue:
        newq = []
        for i, j, keys in queue:
            if keys == (1 << total) - 1:
                return ans
            for ii, jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != "#":
                    kk = keys
                    if grid[ii][jj].islower():
                        kk |= 1 << ord(grid[ii][jj]) - 97
                    if (ii, jj, kk) in seen or grid[ii][jj].isupper() and not kk & (1 << ord(grid[ii][jj]) - 65):
                        continue
                    newq.append((ii, jj, kk))
                    seen.add((ii, jj, kk))
        ans += 1
        queue = newq
    return -1


# grid = ["@.a..", "###.#", "b.A.B"]
# grid = ["@..aA", "..B#.", "....b"]
grid = ["@...a", ".###A", "b.BCc"]
print(shortestPathAllKeys(grid))
