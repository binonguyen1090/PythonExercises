# Write a method count_a(word) that takes in a string word and returns the number of a's in the word. The method should count both lowercase (a) and uppercase (A)
# puts count_a("application")  # => 2
# puts count_a("bike")         # => 0
# puts count_a("Arthur")       # => 1
# puts count_a("Aardvark")     # => 3

def count_a(str):
    str = str.lower()
    count = 0
    for i in range (0, len(str)):
        if str[i] == "a":
            count += 1
    return count


print (count_a("application"))  # => 2
print (count_a("bike")     )    # => 0
print (count_a("Arthur")   )    # => 1
print (count_a("Aardvark") )
