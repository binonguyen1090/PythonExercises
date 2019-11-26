# Consonant Cancel
# Write a method consonant_cancel that takes in a sentence and returns a new sentence where every word begins with it's first vowel.


def cut(string):
  v = 'aeiuo'
  for i in range(0,len(string)):
    if string[i] in v:
      result = string[i:]
      break
  return(string[i:])



def consonant_cancel(sentence):
  splt = sentence.split(' ')
  result = []
  for word in splt:
    result.append(cut(word))
  final = " ".join(result)
  print(final)



consonant_cancel("down the rabbit hole") #=> "own e abbit ole"
consonant_cancel("writing code is challenging") #=> "iting ode is allenging"

