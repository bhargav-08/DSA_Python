# Generate Valid parenthesis from given n  For n=3 we can get  ['((()))', '(()())', '(())()', '()(())', '()()()']


def gbp(n):
    answer = []

    def helper(string, op, cl):
        if op == 0 and cl == 0:
            answer.append(string)
            return

        if op == 0:
            op1 = string + ")"
            helper(op1, op, cl - 1)

        elif cl >= op:
            op1 = string + "("
            op2 = string + ")"
            helper(op1, op - 1, cl)
            helper(op2, op, cl - 1)

    def helper2(string, op, cl):
        if op == 0 and cl == 0:
            answer.append(string)
            return

        if op != 0:
            op1 = string + "("
            helper2(op1, op - 1, cl)

        if cl > op:
            op2 = string + ")"
            helper2(op2, op, cl - 1)

    # helper("(", n - 1, n)
    helper2("(", n - 1, n)
    return answer


print(gbp(3))