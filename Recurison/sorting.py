def i(arr, temp):
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()
    i(arr, temp)
    arr.append(val)


def s(arr):
    if len(arr) == 1:
        return

    val = arr.pop()
    s(arr)
    i(arr, val)


arrr = [2, 1, 0, 5, 90, 2, 190, 23]
# s(arrr)
# print(arrr)

print(6 & 1)
