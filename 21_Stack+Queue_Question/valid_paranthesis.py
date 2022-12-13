
def validParanthesis(s):
    stack = []
    for i in s:
        if i in ["(","{","["]:
            stack.append(i)
        else:
            if stack :
                prev = stack[-1]
                if (i==")" and prev=="(") or (i=="]" and prev=="[") or (i=="}" and prev=="{"):
                    stack.pop()
            else:
                return False

    if len(stack)==0:
        return True
    else:
        return False

s = ")()"
print(validParanthesis(s))