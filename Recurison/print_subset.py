# Print all the Sub Set (power set) of given string => 2^n


def printPermutation(op, ip):
    if len(ip) == 0:
        print(op)
        return

    op1 = op
    op2 = op + ip[0]
    printPermutation(op1, ip[1:])
    printPermutation(op2, ip[1:])


printPermutation("", "abcd")
