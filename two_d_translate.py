
# Two D Translate
# Write a method two_d_translate that takes in a 2 dimensional array and translates it into a 1 dimensional array. You can assume that the inner arrays always have 2 elements. See the examples.


def two_d_translate(arr):
  result = []

  for i in arr:
    for j in range(0, i[1]):
    
      result.append(i[0])
  print(result)



two_d_translate([
  ['boot', 3],
  ['camp', 2],
  ['program', 0]
]) 



two_d_translate([
  ['red', 1],
  ['blue', 4]
])
