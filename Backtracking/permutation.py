def per(nums):
    answer = []

    def solve(index):
        if index == len(nums):
            answer.append(nums[:])
            # print("reached")
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            print(index, i)
            solve(i+1)
            nums[index], nums[i] = nums[i], nums[index]

    solve(0)
    return answer


n = [1, 2, 3]
print(per(n))
