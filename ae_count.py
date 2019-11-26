# Ae Count
# Write a method ae_count that takes in a string and returns a hash containing the number of a's and e's in the string. Assume the string contains only lowercase characters.

def ae_count(str):
  hash = {}
  hash['a'] = 0
  hash['e'] = 0
  for i in str:
    if i =='a':
      hash['a'] += 1
    if i == 'e':
      hash['e'] += 1
  print(hash)


ae_count("everyone can program") #=> {"a"=>2, "e"=>3}
ae_count("keyboard") #=> {"a"=>1, "e"=>1}