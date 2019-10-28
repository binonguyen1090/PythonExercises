# Give an array of integers:
# arr = [100, -101, 200, -3, 1000]
# Find out the biggest sum of 2 integer
# And return the INDEX of those integer

arr = [100, -101, 200, -3, 1000]
max = 0
new = []
for i in range(0, len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if (arr[i]+arr[j] > max):
            max = arr[i]+arr[j]
            new.append(i)
            new.append(j)

print(new[-2:])



