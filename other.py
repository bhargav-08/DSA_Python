def findMinArrowShots(points) -> int:
    points.sort(key=lambda x: x[1])
    answer = 0
    print(points)
    i = 0
    while i < len(points):
        j = i+1
        answer += 1
        while j < len(points) and points[i][1] >= points[j][0]:
            j += 1
        i = j
    # print(points)
    return answer


points = [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
[[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]

[[6, 7], [3, 9], [6, 9], [1, 10], [4, 11], [8, 12], [9, 12]]


# [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
print(findMinArrowShots(points))
