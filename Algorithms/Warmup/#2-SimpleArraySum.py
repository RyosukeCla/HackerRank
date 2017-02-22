import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# buildin function
print(sum(arr))

# or
# sum = 0
# for i in arr:
#   sum += i
# print(sum)
