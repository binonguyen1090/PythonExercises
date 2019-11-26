# Retrieve Values
# Write a method retrieve_values that takes in two hashes and a key. The method should return an array containing the values from the two hashes that correspond with the given key.

def retrieve_values(hash1, hash2, key):
  v1 = hash1[key]
  v2 = hash2[key]
  result = []
  result.append(v1)
  result.append(v2)
  print(result)



retrieve_values({"name":"Fido", "color":"brown"}, {"name":"Spot", "color": "white"}, "name") #=> ["Fido", "Spot"]

retrieve_values({"name":"Fido", "color":"brown"}, {"name":"Spot", "color": "white"}, "color") #=> ["brown", "white"]

