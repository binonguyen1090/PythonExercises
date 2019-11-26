# Combinations
# Write a method combinations that takes in an array of unique elements, the method should return a 2D array representing all possible combinations of 2 elements of the array.

def combinations(arr):
  result = []
  for i in range(0, len(arr)-1):
    for j in range(i+1,len(arr)):
      result.append([arr[i],arr[j]])
  print(result)

combinations([0, 1, 2, 3])

