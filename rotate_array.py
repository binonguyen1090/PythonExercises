# Rotate Array
# Write a method rotate_array that takes in an array and a number. The method should return the array after rotating the elements the specified number of times. A single rotation takes the last element of the array and moves it to the front.

def rotate_array(arr, num):
  i = 0
  while i < num:
    c = arr.pop(-1)
    arr.insert(0,c)

    i+= 1
  print(arr)



rotate_array([ "a", "b", "c", "d" ], 2)
