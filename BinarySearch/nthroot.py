def findNthRootOfM(n, m):
    # Write your Code here.
    ep = 1e-6
    # print(n,m)
    lo = 1
    hi = m

    while hi-lo > ep:
        mid = (lo+hi)/2

        if mid**n > m:
            hi = mid

        else:
            lo = mid

    return lo


print(findNthRootOfM(3, 27))    
print(findNthRootOfM(4, 69))
