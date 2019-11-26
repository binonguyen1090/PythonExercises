

# Array Translate
# Write a method array_translate that takes in an array whose elements alternate between words and numbers. The method should return a string where each word is repeated the number of times that immediately follows in the array.

def array_translate(array):
  result = ""
  i = 0
  while i < len(array):
    result += array[i]*array[i+1]
    i+= 2
  print(result)





array_translate(["Cat", 2, "Dog", 3, "Mouse", 1])
array_translate(["red", 3, "blue", 1])