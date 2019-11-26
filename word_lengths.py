# Word Lengths
# Write a method word_lengths that takes in a sentence string and returns a hash where every key is a word of the sentence, and its' corresponding value is the length of that word.

def word_lengths(sentence):
  splt = sentence.split(' ')
  hash = {}

  for i in splt:
    hash[i] = len(i)
  print(hash)



word_lengths("this is fun") #=> {"this"=>4, "is"=>2, "fun"=>3}
word_lengths("When in doubt, leave it out") #=> {"When"=>4, "in"=>2, "doubt,"=>6, "leave"=>5, "it"=>2, "out"=>3}