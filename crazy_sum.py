# write a method take an array of number
# Return sum of multiply number by index
# crazy_sum([2,]) == 0 /2*0
# crazy_sum([2,3,]) == 3 /2*0 + 3*1
# crazy_sum([2,3,5,]) == 13 /2*0 + 3*1 + 5*2
# crazy_sum([2,3,5,2]) == 19 /2*0 + 3*1 + 5*2 + 2*3
#


def get(list):

    sum = 0
    for i in range(len(list)):
        sum += (list[i]*i)
    return sum
print(get([2,3,5,2]))