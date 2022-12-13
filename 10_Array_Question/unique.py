l = [1,2,3,4,5,6,2,23]

def hasUnique(arr):
    s = set(arr)
    if len(arr)==len(s):
        print("Given array has all unique element")
    else:
        print("Given array has duplicate element")
    
hasUnique(l)