def test(one,two=[]):
    one = one +1
    two.append(one)
    return two
   
print(test(2))
print(test(4))
