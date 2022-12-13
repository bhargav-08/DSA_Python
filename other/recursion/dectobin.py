def decToBin(num):
    if num==0:
        return ""
    return decToBin(num//2) + str(num%2)


# print(decToBin(742))

print(1 is 2)
