# Print all the permutation of given array
# Input- [1,2,3] # Output-[[1,2,3],[1,3,2],[2,1,3],[3,1,2],[2,3,1],[3,2,1]]


def printPermutation(arr):
    answer = []

    def solve(index):
        if index >= len(arr):
            answer.append(arr[:])
            return

        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            solve(index + 1)
            arr[i], arr[index] = arr[index], arr[i]

    solve(0)
    return answer


arr = [1, 2, 3]
print(printPermutation(arr))
