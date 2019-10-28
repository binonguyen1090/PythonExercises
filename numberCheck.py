# Write a method number_check(num) that takes in a number and returns a string. The method should return the string 'positive' if the num is positive, 'negative' if the num is negative, and 'zero' if the num is zero.
# puts number_check(5)    # => "positive"
# puts number_check(-2)   # => "negative"
# puts number_check(0)    # => "zero"

def number_check(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

print(number_check(0))