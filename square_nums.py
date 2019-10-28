# Write method take a number max
# return perfect sqaure less than max
# No math or **
# sqaure(5) == 2
# square(10) == 3
# square(25) == 4



def get(num):
    i = 1
    result = i*i
    while result < num:
        i+=1
        result = i*i
    return(i-1)

print(get(101))
