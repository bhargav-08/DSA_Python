from pprint import pprint

__all__ = ["lcs2d", "pprint"]


def lcsRecursive(x, y, lx, ly):
    try:
        lcsRecursive.count += 1
    except:
        lcsRecursive.count = 1
    if lx == 0 or ly == 0:
        return 0
    elif x[lx - 1] == y[ly - 1]:
        return 1 + lcsRecursive(x, y, lx - 1, ly - 1)  # type:ignore
    elif x[lx - 1] != y[ly - 1]:
        return max(lcsRecursive(x, y, lx, ly - 1),
                   lcsRecursive(x, y, lx - 1, ly))


def lcsMemo(x, y, lx, ly):
    try:
        lcsMemo.count += 1
    except:
        lcsMemo.count = 1
    if lx == 0 or ly == 0:
        return 0
    if t[lx][ly] != -1:
        return t[lx][ly]
    elif x[lx - 1] == y[ly - 1]:
        t[lx][ly] = 1 + lcsMemo(x, y, lx - 1, ly - 1)  # type:ignore
        return t[lx][ly]
    elif x[lx - 1] != y[ly - 1]:
        t[lx][ly] = max(
            lcsMemo(x, y, lx, ly - 1),  # type: ignore
            lcsMemo(x, y, lx - 1, ly))  # type: ignore
        return t[lx][ly]


def lcs2d(x, y):
    lcs2d.t = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                lcs2d.t[i][j] = 1 + lcs2d.t[i - 1][j - 1]
            elif x[i - 1] != y[j - 1]:
                lcs2d.t[i][j] = max(lcs2d.t[i][j - 1], lcs2d.t[i - 1][j])
    # pprint(t)
    return lcs2d.t[-1][-1]


if __name__ == "__main__":
    x = "abcdgh"
    y = "abedfgha"
    print(lcsRecursive(x, y, len(x), len(y)))
    # print("Count", lcsRecursive.count)

    t = [[-1 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    print(lcsMemo(x, y, len(x), len(y)))
    # print("Count", lcsMemo.count)

    print(lcs2d(x, y))
