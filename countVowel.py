# Write a method, count_vowels(word), that takes in a string word and returns the number of vowels in the word. Vowels are the letters a, e, i, o, u.
#
# puts count_vowels("bootcamp")  # => 3
# puts count_vowels("apple")     # => 2
# puts count_vowels("pizza")     # => 2
#
def count_vowels(str):
    v = "aeoiu"
    count = 0
    for i in range (0,len(str)):
        if v.__contains__(str[i]):
            count +=1
    return count
print (count_vowels("bootcamp"))  # => 3
print (count_vowels("apple"))    # => 2
print (count_vowels("pizza"))
