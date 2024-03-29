# Write a method element_times_index(nums) that takes in an array of numbers and returns a new array containing every number of the original array multiplied with its index.
#
# print element_times_index([4, 7, 6, 5])       # => [0, 7, 12, 15]
# puts
# print element_times_index([1, 1, 1, 1, 1, 1]) # => [0, 1, 2, 3, 4, 5]

def element_times_index(arr):
    result = []
    for i in range (0,len(arr)):
        result.append(arr[i]*i)
    return result

print(element_times_index([4, 7, 6, 5]) )      # => [0, 7, 12, 15]

print(element_times_index([1, 1, 1, 1, 1, 1])) # => [0, 1, 2, 3, 4, 5
