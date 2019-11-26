# Pick Primes
# Write a method pick_primes that takes in an array of numbers and returns a new array containing only the prime numbers.


def prime(n):
  for i in range( 2, n):
    if n % i  == 0:
      return False
  return True

def pick(arr):
  result = []
  for i in arr:
  
    if prime(i):
      result.append(i)
  print(result)

pick(([2, 3, 4, 5, 6]))
pick([101, 20, 103, 2017])