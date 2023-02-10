def isAlienSorted(words, order):
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    print(words)
    # print(list(zip(words, words[1:])))
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


def isAlienSorted1(words, order):
    return words == sorted(words, key=lambda w: map(order.index, w))


words = ["hello", "leetcode", "other", "another"]
order = "hlabcdefgijkmnopqrstuvwxyz"

# print(isAlienSorted(words, order))

l1 = [1, 2, 3]
l2 = [1, 2, 3, 4]


print(l1 > l2)
