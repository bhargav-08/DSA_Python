# n = int(input())
n = 1
for i in range(n):
    size = int(input())
    arr = [int(item) for item in input().strip().split()]

    p1 = arr[0]
    p2 = 1
    k = 1

    for i in arr[1:]:
        p2 *= i

    while k < size and p1 != p2:
        k += 1
        p1 = p1 * arr[k-1]
        p2 = p2/arr[k-1]

    if p1 != p2:
        print(-1)
    else:
        print(k)
