d1 = {}.fromkeys([1,2,3,4,45],3)
# print(d1)

# print(d1.setdefault('one','ek'))
# print(d1)
# print(d1.pop(20,"Default Value"))
print(d1.popitem()) # removes last item and return as tuple
# print(d1)