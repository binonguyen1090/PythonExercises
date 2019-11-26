# Element Count
# Write a method element_count that takes in an array and returns a hash representing the count of each element in the array.

def element_count(arr):
  new = []
  hash = {}
  for i in arr:
    if i not in new:
      new.append(i)
  for j in new:
    hash[j] = 0
  for ele in arr:
    hash[ele] += 1
  print(hash)



element_count(["a", "b", "a", "a", "b"]) #=> {"a"=>3, "b"=>2}
element_count(["red", "red", "blue", "green"]) #=> {"red"=>2, "blue"=>1, "green"=>1}