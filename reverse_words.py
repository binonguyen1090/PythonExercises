# Reverse Words
# Write a method reverse_words that takes in a sentence string and returns the sentence with the order of the characters in each word reversed. Note that we need to reverse the order of characters in the words, do not reverse the order of words in the sentence.

def reverse(str):
  new = ""
  for i in str:
    new = i + new
  return(new)


def reverse_words(sent):
  splt = sent.split(' ')
  result = []

  for word in splt:
    new_word = reverse(word)
    result.append(new_word)

  result = " ".join(result)
  print(result)

reverse_words('simplicity is prerequisite for reliability')