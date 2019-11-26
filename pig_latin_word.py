# Pig Latin Word
# Write a method pig_latin_word that takes in a word string and translates the word into pig latin.

def pig_latin_word(word):
  v = "ieuao"
  if word[0] in v:
    new = word + 'yay'
    print(new)
  else:
    index = 0
    while index < len(word):
      if word[index] in v:
        break
      index += 1


    new = word[index:] + word[0:index] + 'ay'

    print(new)


pig_latin_word("apple")   # => "appleyay"
pig_latin_word("eat")     # => "eatyay"
pig_latin_word("banana")  # => "ananabay"
pig_latin_word("trash")   # => "ashtray"