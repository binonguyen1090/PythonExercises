# Two D Sum
# Write a method two_d_Sum that takes in a two dimensional array and returns the sum of all elements in the array.

def two_d_sum(arr):
  total = 0
  for i in arr:
    for e in i:
      total += e

  print(total)

two_d_sum([
  [4, 5],
  [1, 3, 7, 1]
])    # => 21

two_d_sum([
  [3, 3],
  [2],
  [2, 5]
])    # => 15