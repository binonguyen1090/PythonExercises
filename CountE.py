# Write a method count_e(word) that takes in a string word and returns the number of e's in the word
# puts count_e("movie") # => 1
# puts count_e("excellent") # => 3

def count_e(w):
    count = 0
    i = 0
    while i < len(w):
        if w[i] == "e":
            count += 1
        i+= 1
    return count

print(count_e("movie")) # => 1
print(count_e("excellent")) # => 3
