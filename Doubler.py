# Write a method doubler(numbers) that takes an array of numbers and returns a new array
# where every element of the original array is multiplied by 2.
#
# print doubler([1, 2, 3, 4]) # => [2, 4, 6, 8]
# puts
# print doubler([7, 1, 8])    # => [14, 2, 16]

def doubler(arr):
    new = []

    for i in range(0,len(arr)):
        new.append(arr[i]*2)
    return new

print (doubler([1, 2, 3, 4])) # => [2, 4, 6, 8]

print (doubler([7, 1, 8]))    # => [14, 2, 16]
