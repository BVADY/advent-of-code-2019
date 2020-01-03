import time

day = "1"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

res = 0;
for line in inFile:
  res += int(line) / 3 - 2

print(res)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))