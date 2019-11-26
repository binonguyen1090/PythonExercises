# Double Letter Count
# Write a method that takes in a string and returns the number of times that the same letter repeats twice in a row.

def double_letter_count(string):
  splt = string.split(' ')
  count = 0
  for i in splt:
    for j in range (0, len(i)-1):
      if i[j] == i[j+1]:
        count += 1
  print(count)



double_letter_count("the jeep rolled down the hill") #=> 3
double_letter_count("bootcamp") #=> 1