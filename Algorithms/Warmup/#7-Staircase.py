import sys


n = int(input().strip())

for i in range(n):
  stair = ""
  for j in range(n):
    if n - i - 1 > j:
      stair += " "
    else:
      stair += "#"
  print(stair)
