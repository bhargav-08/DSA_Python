def solve(A, B):
    m = {}
    cnt = 0

    xr = 0

    for num in A:
        xr = xr ^ num
        if xr == B:
            cnt += 1

        y = xr ^ B
        if y in m:
            cnt = cnt+m[y]

        if xr in m:
            m[xr] += 1
        else:
            m[xr] = 1

    return cnt


A = [5, 6, 7, 8, 9]
B = 5
print(solve(A, B))
