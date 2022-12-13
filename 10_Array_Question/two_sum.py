def twoSum(array,target):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return(i,j)
    return "Target is not present in array"

def otherway(array,target):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                return(i,j)
    return "Target is not present in array"

# print(twoSum([5,10,7,3,5],10))
# print(otherway([5,10,7,3,5],10))
    
# print(range(5,5))
