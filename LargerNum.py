# Write a method larger_number(num1, num2) that takes in two numbers and returns the larger of the two numbers.
# puts larger_number(42, 28)   # => 42
# puts larger_number(99, 100)  # => 100

def larger_number(a,b):
    if a > b:
        return a
    else:
        return b

print (larger_number(42, 28))   # => 42
print (larger_number(99, 100))  # => 100