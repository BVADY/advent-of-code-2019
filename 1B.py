import time

day = "1B"

inFile = open('inputs/{}.in'.format(day), "r")

start_time = time.time()

def calcFuel(f):
  x = (f / 3) - 2
  if(x > 0):
    return f + calcFuel(x)
  else:
    return f
    
print(sum((calcFuel(int(x)) -int(x)) for x in inFile))
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))