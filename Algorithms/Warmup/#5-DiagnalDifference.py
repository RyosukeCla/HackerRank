import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diagnal0 = 0
diagnal1 = 0
for i in range(n):
  diagnal0 += a[i][i]
  diagnal1 += a[i][n-i-1]

print(abs(diagnal0 - diagnal1))
