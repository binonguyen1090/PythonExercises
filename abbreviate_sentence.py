# Abbreviate Sentence
# Write a method abbreviate_sentence that takes in a sentence string and returns a new sentence where every word longer than 4 characters has all of it's vowels removed.

def abbreviate_sentence(sent):
  v = "ioaeu"
  split_arr = sent.split(' ')
  
  arr = []
  for word in split_arr:
    if len(word) <= 4:
      arr.append(word)
    else:
      new = ""
      for i in word:
        if i not in v:
          new += i
          

      arr.append(new)
  arr = " ".join(arr)
  print(arr)


abbreviate_sentence("what a wonderful life")

