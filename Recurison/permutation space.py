# Create all the permutation with space like for input "ABC" print ["ABC","A_BC","AB_C","A_B_C"]


def permutationSpace(ip):

    def helper(ip, op):
        if len(ip) == 0:
            if op[-1] != " ":
                print(op)
            return

        op1 = op + ip[0] + " "
        op2 = op + ip[0]
        helper(ip[1:], op1)
        helper(ip[1:], op2)

    helper(ip, "")


permutationSpace("abc")