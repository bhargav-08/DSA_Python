def reverseString(string):
    if len(string)==0:
        return ""
    return (reverseString(string[1:]) + string[0])

def isPalindrome(string):
    result = reverseString(string)
    return result==string


print(reverseString("bhargav"))
print(isPalindrome("  "))


