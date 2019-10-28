# Write a method longer_string(str1, str2) that takes in two strings and returns the longer of the two strings. In the case of a tie, the method should return the first string.
# puts longer_string("app", "academy") # => "academy"
# puts longer_string("summer", "fall") # => "summer"
# puts longer_string("hello", "world") # => "hello"


def longer_string(a, b):
    if len(a) > len(b):
        return a
    elif len(a) == len(b):
        return a
    else:
        return b

print(longer_string("summer", "fall"))