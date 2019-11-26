# Is Valid Email
# Write a method is_valid_email that takes in a string and returns a boolean indicating whether or not it is a valid email address.

def is_valid_email(str):
  if '@' not in str:
    print(False)
    return False
  splt = str.split('@')
  alpha = "abcdefghijklmnopqrstuvwxyz"
  for i in splt[0]:
    if i not in alpha:
      print(False)
      return False
  if '.' not in splt[1]:
    print(False)
    return False
  docsplt = splt[1].split('.')
  if len(docsplt) == 2:
    print(True)
    return True
  else:
    print(False)
    return False


is_valid_email("abc@xy.z")         # => true
is_valid_email("jdoe@gmail.com")   # => true
is_valid_email("jdoe@g@mail.com")  # => false
is_valid_email("jdoe42@gmail.com") # => false
is_valid_email("jdoegmail.com")    # => false
is_valid_email("az@email")         # => false

