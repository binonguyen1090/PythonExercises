# Write a method factorial(num) that takes in a number num and returns the product of all numbers from 1 up to and including num.
#
# puts factorial(3) # => 6, because 1 * 2 * 3 = 6
# puts factorial(5) # => 120, because 1 * 2 * 3 * 4 * 5 = 120

def factorial(max):
    total = 1;
    for i in range (1, max +1):
        total *= i
    return total

print(factorial(3)) # => 6, because 1 * 2 * 3 = 6
print(factorial(5)) # => 120, because 1 * 2 * 3 * 4 * 5 = 120