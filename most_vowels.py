# Most Vowels
# Write a method most_vowels that takes in a sentence string and returns the word of the sentence that contains the most vowels.

def most_vowels(sentence):

  v = ' oieua'
  words = sentence.split(' ')
  max = 0
  w = sentence[0]
  for i in range(0,len(words)):
    count = 0
    for j in words[i]:
      if j in v:
        count += 1
    if count > max:
      max = count
      w = words[i]
  print(w)



most_vowels("what a wonderful life") #=> "wonderful"