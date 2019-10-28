# Write a method reverse(word) that takes in a string word and returns the word with its letters in reverse order.
#
# puts reverse("cat")          # => "tac"
# puts reverse("programming")  # => "gnimmargorp"
# puts reverse("bootcamp")     # => "pmactoob"
#

def reverse(word):
    new = ""
    for i in range (0, len(word)):
        new = word[i] + new
    return new

print(reverse("cat"))          # => "tac"
print(reverse("programming"))  # => "gnimmargorp"
print(reverse("bootcamp"))     # => "pmactoob"
#