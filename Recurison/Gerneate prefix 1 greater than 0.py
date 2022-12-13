def prefixGenerator(n):

    def helper(n, one, zero, result):
        if n == 0:
            print(result)
            return

        if zero + 1 <= one:
            answer = result + "0"
            helper(n - 1, one, zero + 1, answer)

        if one + 1 > zero:
            answer = result + "1"
            helper(n - 1, one + 1, zero, answer)

    helper(n, 0, 0, "")


prefixGenerator(3)