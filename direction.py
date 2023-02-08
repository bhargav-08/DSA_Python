def subsetXORSum(nums) -> int:
    answer = 0

    def solve(index, arr):
        # nonlocal answer
        if index >= len(arr):
            #     temp = 0
            #     for item in arr:
            #         temp^=item
            #     answer+=temp
            #     return
            print(arr)
            return

        solve(index+1,arr)
        arr.append(nums[index])
        solve(arr, index+1)

    solve(0, [])
    return answer


nums = [5, 1, 6]
subsetXORSum(nums)
# print(subsetXORSum(nums))
