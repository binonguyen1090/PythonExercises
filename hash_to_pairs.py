
# Hash To Pairs
# Write a method hash_to_pairs that takes in a hash and returns a 2D array representing each key-value pair of the hash.

def hash_to_pairs(hash):
  result = []
  for i in hash:
    c = [i, hash[i]]
    result.append(c)
  print(result)

hash_to_pairs({"name":"skateboard", "wheels":4, "weight":"7.5 lbs"}) #=> [["name", "skateboard"], ["wheels", 4], ["weight", "7.5 lbs"]]



hash_to_pairs({"kingdom":"animalia", "genus":"canis", "breed":"German Shepherd"}) #=> [["kingdom", "animalia"], ["genus", "canis"], ["breed", "German Shepherd"]]
