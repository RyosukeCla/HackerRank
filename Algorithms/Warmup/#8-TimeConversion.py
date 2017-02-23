import sys


time = input().strip()
ampm = time[-2:]
times = time[:-2].split(':')
if (ampm == "PM"):
  times[0] = int(times[0]) % 12 + 12
else:
  times[0] = int(times[0]) % 12

if (times[0] < 10):
  times[0] = "0{0}".format(times[0])

print("{0}:{1}:{2}".format(times[0], times[1], times[2]))
