# Pyramid Sum
# Write a method pyramid_sum that takes in an array of numbers representing the base of a pyramid. The function should return a 2D array representing a complete pyramid with the given base. To construct a level of the pyramid, we take the sum of adjacent elements of the level below.


# For example, the base [1, 4, 6] gives us the following pyramid
#     15
#   5   10
# 1   4    6

def get(arr):
  
  result = []
  for i in range(0,len(arr)-1):
    total = arr[i] + arr[i+1]
    result.append(total)
  return(result)


def pyramid_sum(base):
  l = len(base) -1 
  result = [base]
  i = 0
  while i < l:
    result.insert(0,get(base))
    base = get(base)
    i+=1
  
  print(result)
  



pyramid_sum([1, 4, 6]) #=> [[15], [5, 10], [1, 4, 6]]


pyramid_sum([3, 7, 2, 11]) #=> [[41], [19, 22], [10, 9, 13], [3, 7, 2, 11]]