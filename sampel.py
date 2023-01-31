from collections import OrderedDict

d = OrderedDict()

d[1] = "one"
d[2] = "two"
d[3] = "three"
d[4] = "four"

print(d)

d[2] = "change"
print(d)
