# Vowel Cipher
# Write a method vowel_cipher that takes in a string and returns a new string where every vowel becomes the next vowel in the alphabet.


def vowel_cipher(string):
  v = "aeiou"
  new_string = ""

  for i in string:
    if i not in v:
      new_string+= i
    else:
      old_i = v.index(i)
      new_char = v[(old_i+1) % 5]
      new_string += new_char
  print(new_string)
vowel_cipher("bootcamp") #=> buutcemp
vowel_cipher("paper cup") #=> pepir cap