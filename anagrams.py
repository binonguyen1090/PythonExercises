# Anagrams
# Write a method anagrams? that takes in two words and returns a boolean indicating whether or not the words are anagrams. Anagrams are words that contain the same characters but not necessarily in the same order. Solve this without using .sort

def anagrams(word1, word2):
  if len(word1) != len(word2):
    print(False)
    return(False)
  
  hash = {}

  for i in word1:
    if i in hash:
      hash[i] += 1
    else:
      hash[i] = 1
  
  for j in word2:
    if j in hash:
      hash[j] -= 1
    else:
      hash[j] = 1
  
  for h in hash:
    if hash[h] != 0:
      print(False)
      return(False)
  print(True)
  return(True)





anagrams("cat", "act")          #=> true
anagrams("restful", "fluster")  #=> true
anagrams("cat", "dog")          #=> false
anagrams("boot", "bootcamp")    #=> false