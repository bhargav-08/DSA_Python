# def nextGreaterElement(n):
#     digits = list(str(n))
#     i = len(digits) - 1
#     while i-1 >= 0 and digits[i] <= digits[i-1]:
#         i -= 1

#     if i == 0:
#         return -1

#     j = i
#     while j+1 < len(digits) and digits[j+1] > digits[i-1]:
#         j += 1

#     digits[i-1], digits[j] = digits[j], digits[i-1]
#     digits[i:] = digits[i:][::-1]
#     ret = int(''.join(digits))

#     return ret if ret < 1 << 31 else -1

def nextGreaterElement(n: int) -> int:
    num = [int(x) for x in str(n)]

    j = len(num)-1
    while j-1 >= 0 and num[j] <= num[j-1]:
        j -= 1

    if j == 0:
        return -1
    
    pivot = num[j-1]

    i = len(num)-1
    while i >= j and pivot > num[i]:
        i -= 1
    print(i, j)

    num[i], num[j-1] = num[j-1], num[i]
    num[j:] = num[j:][::-1]
    return int("".join(num))


print(nextGreaterElement(230241))
