import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(sum(arr))

# python can handle very big integer.
# But if you use the other language like Java,
# you need to use " long " primitive variable.
