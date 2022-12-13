def customSum(n):
    if n==0:
        return 0
    return n+customSum(n-1)

print(customSum(2))