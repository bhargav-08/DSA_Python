from bisect import bisect_right


def matrixMedian(matrix):
    l = len(matrix)*len(matrix[0])//2

    def count(value):
        result = 0
        for i in matrix:
            result += bisect_right(i, value)

        return result

    low = 1
    high = max(map(max, matrix))
    print(high)

    print(high)
    while low <= high:
        mid = low+high >> 1
        # print(count(mid))
        if count(mid) > l:
            high = mid-1
        else:
            low = mid+1

    return low


matrix = [[2, 6, 9], [1, 5, 11], [3, 7, 8]]
print(matrixMedian(matrix))


