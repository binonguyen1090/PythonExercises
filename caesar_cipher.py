# Caesar Cipher
# Write a method caesar_cipher that takes in a string and a number. The method should return a new string where every character of the original is shifted num characters in the alphabet



def caesar_cipher(str, num):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  new_string = ""
  for ch in str:
    old_i = alphabet.index(ch)
    new_i = (old_i + num)% 26
    new_ch = alphabet[new_i]
    new_string += new_ch
  print(new_string)



caesar_cipher("apple", 1)    #=> "bqqmf"
caesar_cipher("bootcamp", 2) #=> "dqqvecor"
caesar_cipher("zebra", 4)    #=> "difve"
