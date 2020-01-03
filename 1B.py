import time

day = "1B"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

def calcFuel(f):
  x = (f / 3) - 2
  if(x > 0):
    return f + calcFuel(x)
  else:
    return f
    
res = 0
for line in inFile:
  res += calcFuel(int(line)) - int(line)

print(res)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))