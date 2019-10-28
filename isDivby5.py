# puts is_div_by_5(10) # => true
# puts is_div_by_5(40) # => true
# puts is_div_by_5(42) # => false
# puts is_div_by_5(8)  # => false

def is_div_by_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

print(is_div_by_5(40))