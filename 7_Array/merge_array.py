
def merge(intervals):
    answer = []
    intervals.sort()

    for item in intervals:

        if not answer:
            answer.append(item)

        if answer[-1][1] < item[0] and answer[-1][1] < item[1]:
            answer.append(item)

        if answer[-1][-1] < item[-1]:
            answer[-1][-1] = item[-1]

        if answer[-1][0] > item[0]:
            answer[-1][0] = item[0]

    return answer


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
