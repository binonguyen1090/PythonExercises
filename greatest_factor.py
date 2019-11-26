# Greatest Factor Array
# Write a method greatest_factor_array that takes in an array of numbers and returns a new array where every even number is replaced with it's greatest factor. A greatest factor is the largest number that divides another with no remainder. For example the greatest factor of 16 is 8. (For the purpose of this problem we won't say the greatest factor of 16 is 16, because that would be too easy, ha)


def check(n):
  for i in range(n-1,1,-1):
    if n % i == 0:
       return(i)
 


def greatest_factor_array(arr):
  result = []
  for i in arr:
    if i % 2 == 0:
      result.append(check(i))
    else:
      result.append(i)
  print(result)



greatest_factor_array([16, 7, 9, 14]) # => [8, 7, 9, 7]
greatest_factor_array([30, 3, 24, 21, 10]) # => [15, 3, 12, 21, 5]
