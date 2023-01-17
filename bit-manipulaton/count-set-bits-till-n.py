import cProfile

#
#
#
#
#
#
# print([]+[])

with cProfile.Profile() as profile:
    answer = 0
    for i in range(1000):
        answer = i+i
        print(answer)


profile.print_stats()

#
