def isAlienSorted(words, order):
    m = {c: i for i, c in enumerate(order)}
    words = [[m[c] for c in w] for w in words]
    return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


def isAlienSorted1(words, order):
    return words == sorted(words, key=lambda w: map(order.index, w))


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(words, order))
