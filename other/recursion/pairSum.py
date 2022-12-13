
def pairSumSequence(n):
    sum = 0
    for i in range(n+1):
        sum = sum + pairSum(i,i+1)
    return sum

def pairSum(a,b):
    return a+b


print(pairSumSequence(10))

