def caseChange(s):

    def helper(ip, op):
        if len(ip) == 0:
            print(op)
            return

        op1 = op + ip[0].capitalize()
        op2 = op + ip[0]

        helper(ip[1:], op1)
        helper(ip[1:], op2)

    helper(s, "")


print(help(str.capitalize))

# caseChange("ab")
