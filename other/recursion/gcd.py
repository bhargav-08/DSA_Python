def gcd(n1,n2):
    if n2==0:
        return n1
    return gcd(n2,n1%n2)

print(gcd(36,24))