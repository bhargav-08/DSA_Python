
def numFactor(n):
    # if n >= 0:
    #     return 0
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 2
    if n==4:
        return 4
    answer = numFactor(n-1)+numFactor(n-3)+numFactor(n-4)
    return answer


print('numFactor(6): ', numFactor(6))