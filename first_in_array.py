

#First In Array
# Write a method first_in_array that takes in an array and two elements, the method should return the element that appears earlier in the array.

def first(arr,st1,st2):
  pos1 = 0
  pos2 = 0

  for i in arr:
    if i == st1:
      pos1 =i
    elif i == st2:
      pos2 = i
  if pos1 > pos2:
    print(st2)
  if pos2 > pos1:
    print(st1)
first(["a", "b", "c", "d"], "d", "b")