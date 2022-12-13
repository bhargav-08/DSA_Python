def permutation(str):
    answer = []
    used = [0 for _ in range(len(str))]

    def solve(s, l):
        if len(s) == len(str):
            answer.append(s[:])
            return

        for index, i in enumerate(l):
            if i == 0:
                l[index] = 1
                solve(s+str[index], l)
                l[index] = 0

    solve("", used)
    return answer


str = "abc"
print(permutation(str))
