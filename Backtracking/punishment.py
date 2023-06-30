from math import log10, sqrt


def punishment(num: int):

    n = int(log10(num))+1

    def s(idx, total):
        if total == sqrt(num) and idx == n:
            return True
        if total > num or idx == n:
            return False

        for i in range(idx, n):
            total = total + int(str(num)[idx:i+1])
            if (s(i+1, total)):
                return True
            total = total - int(str(num)[idx:i+1])
        return False

    return s(0, 0)


print(punishment(37))
