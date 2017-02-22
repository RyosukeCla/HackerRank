import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

def compare(a, b):
  if a > b:
    return [1, 0]
  elif a < b:
    return [0, 1]
  else:
    return [0, 0]

scores = compare(a0, b0)
scores = [x + y for (x, y) in zip(scores, compare(a1, b1))]
scores = [x + y for (x, y) in zip(scores, compare(a2, b2))]

print("%d %d"%(scores[0], scores[1]))
