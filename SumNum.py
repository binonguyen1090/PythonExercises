# //Write a method sum_nums(max) that takes in a number max and returns the sum of all numbers from 1 up to and including max.
# //puts sum_nums(4) # => 10, because 1 + 2 + 3 + 4 = 10
# //puts sum_nums(5) # => 15
def sum_nums(max):
    total = 0;
    for i in range (0, max +1):
        total += i
    return total


print(sum_nums(4)) # => 10, because 1 + 2 + 3 + 4 = 10
print(sum_nums(5)) # => 15