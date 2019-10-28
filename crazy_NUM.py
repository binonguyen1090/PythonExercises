# Write method take a number max
# return perfect sqaure less than max
# No math or **
# sqaure(5) == 2
# square(10) == 3
# square(25) == 4


def crazy_nums(max_num):
    arr = []
    for i in range(1, max_num):

        if (i % 3 == 0 or i % 5 == 0):
            if (i % 15 != 0):
                arr.append(i)

    return (arr)

print(crazy_nums(20))