# Write a method word_check(word) that takes in a word and returns a string. The method should return the string "long" if the word is longer than 6 characters, "short" if it is less than 6 characters, and "medium" if it is exactly 6 characters long.
# puts word_check("contraption") # => "long"
# puts word_check("fruit")       # => "short"
# puts word_check("puzzle")      # => "medium"


def word_check(w):
    if len(w) > 6:
        return "long"
    elif len(w) < 6:
        return "short"
    else:
        return "medium"

print(word_check("puzz111111111"))