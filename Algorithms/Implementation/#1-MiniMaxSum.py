import sys


a,b,c,d,e = input().strip().split(' ')
values = [int(a),int(b),int(c),int(d),int(e)]

sum = sum(values)
max = 0
min = sum
for value in values:
  temp = sum - value
  if (max < temp):
    max = temp
  if (min > temp):
    min = temp

print("{0} {1}".format(min, max))
