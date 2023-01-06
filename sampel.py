from collections import Counter


def minimumRounds(tasks):
    freq = Counter(tasks).values()
    print(freq)
    return -1 if 1 in freq else sum((a + 2) // 3 for a in freq)


def minimumRounds(tasks) -> int:
    freq = Counter(tasks).values()
    answer = 0

    for i in freq:
        if i == 1:
            return -1
        else:
            answer += (i+2)//3

    return answer


tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
print(minimumRounds(tasks))
