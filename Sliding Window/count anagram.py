from collections import defaultdict, Counter


def search(pat, txt):

    pC = Counter(pat)
    res = []
    window = None

    for i in range(len(txt)-len(pat)+1):
        if i == 0:
            window = Counter(txt[:len(pat)])
        else:
            minus = {txt[i-1]: 1}
            plus = {txt[i+len(pat)-1]: 1}
            window += plus
            window -= minus

        if window == pC:
            res.append(i)
    return res


txt = "forxxorfxdofr"
pat = "for"
# print(search(pat, txt))

l = []

print(l+3)
