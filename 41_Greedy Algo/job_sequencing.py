

from collections import namedtuple


def JobScheduling(jobs, n):

    # code here
    answer = 0
    mp = {}
    jobs.sort(key=lambda x: x.profit, reverse=True)

    for job in jobs:
        dl = job.deadline
        profit = job.profit

        if dl not in mp:
            mp[dl] = profit
            answer += profit
        else:
            temp = dl-1
            while temp > 0 and temp in mp:
                temp -= 1

            if temp > 0:
                mp[temp] = profit
                answer += profit

    return len(mp), answer


Jobs = namedtuple("Jobs", "id deadline profit")
j = [Jobs(1, 2, 100), Jobs(2, 1, 19), Jobs(
    3, 2, 27), Jobs(4, 1, 25), Jobs(5, 1, 15)]

print(JobScheduling(j, 5))
