from pprint import pprint


def f(i, j, isTrue):

    if i > j:
        return 0

    if i == j:
        if isTrue:
            return s[i] == "T"
        else:
            return s[i] == "F"

    if t[isTrue][i][j] != -1:
        return t[isTrue][i][j]

    ways = 0

    for k in range(i + 1, j, 2):
        lt = f(i, k - 1, 1)
        lf = f(i, k - 1, 0)

        rt = f(k + 1, j, 1)
        rf = f(k + 1, j, 0)

        if s[k] == "&":
            if isTrue:
                ways += lt * rt  # type: ignore
            else:
                ways += (rt * lf + rf * lt + rf * lf)  # type: ignore

        elif s[k] == "|":
            if isTrue:
                ways += (lt * rt + lf * rt + lt * rf)  # type: ignore
            else:
                ways += (rf * lf)  # type: ignore

        elif s[k] == "^":
            if isTrue:
                ways += (rf * lt + rt * lf)  # type: ignore
            else:
                ways += (rt * lt + rf * lf)  # type: ignore

    t[isTrue][i][j] = ways

    return ways


s = ""
s = "T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F"
# s = "T"
t = [[[-1 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
     for _ in range(2)]
print(f(0, len(s) - 1, 1) % 1003)
