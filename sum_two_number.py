times = int(input())
# times = 1


def sumOfDigits(num):
    s = 0

    for char in str(num):
        s = s + int(char)

    return s


for i in range(times):
    n = int(input())

    x = n//2
    y = n-x

    p1 = sumOfDigits(x)
    p2 = sumOfDigits(y)

    if abs(p1 - p2) > 1:
        if p1 < p2:
            x -= 1
        else:
            y -= 1

    print(x, y)
