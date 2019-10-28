# Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, false otherwise. A palindrome is a word that is spelled the same forwards and backwards.
#
# puts is_palindrome("racecar")  # => true
# puts is_palindrome("kayak")    # => true
# puts is_palindrome("bootcamp") # => false

def is_palindrome(word):
    new = ""
    for i in range (0, len(word)):
        new = word[i] + new
    if new == word:
        return True
    else:
        return False

print (is_palindrome("racecar"))  # => true
print (is_palindrome("kayak"))    # => true
print (is_palindrome("bootcamp")) # => false