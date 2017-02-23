import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

res1 = 0
res2 = 0
res3 = 0
for a_i in arr:
  if (a_i > 0):
    res1 += 1
  elif (a_i < 0):
    res2 += 1
  else:
    res3 += 1

print(res1/n)
print(res2/n)
print(res3/n)
