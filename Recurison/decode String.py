import collections


def decodeString(s: str) -> str:
    stack = collections.deque()

    for i in range(len(s)):
        if s[i] != "]":
            stack.append(s[i])
        else:
            string = ""
            while not stack[-1].isdigit() and stack[-1] != "[":
                val = stack.pop()
                string += val

            number = ""
            stack.pop()
            while stack and stack[-1].isdigit():
                val = stack.pop()
                number += val

            stack.append(int(number[::-1])*string)

    answer = ""
    while stack:
        val = stack.pop()
        answer += val

    return answer[::-1]


s = "3[a]2[bc]"
# s = "3[a2[c]]"
# s = "2[abc]3[cd]ef"
# s = "100[leetcode]"
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(decodeString(s))
