def flatten(arr,temp=[]):
    if len(arr)==0:
        return temp
    if type(arr[0])==int:
        temp.append(arr[0])
        
    elif type(arr[0])==list:
       temp.append(flatten(arr[0]))
        
    return flatten(arr[1:])
    
l = flatten([1,2,3,[4,5,6,8]])

print(l)