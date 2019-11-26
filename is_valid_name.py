# Is Valid Name
# Write a method is_valid_name that takes in a string and returns a boolean indicating whether or not it is a valid name.


def format_name(str):
  name_split = str.split(' ')
  result = []
  for word in name_split:
    new =  word[0].upper() + word[1:].lower()
    result.append(new)
  result = " ".join(result)
  return(result)




def is_valid_name(str):
  splt = str.split(' ')
  if len(splt) < 2:
    print(False)
    return(False)
  else:
    new_name = format_name(str)
    if new_name == str:
      print(True)
      return True
    else:
      print(False)
      return False

is_valid_name("ROBERT DOWNEY JR")


