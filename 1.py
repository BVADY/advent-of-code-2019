import time

day = "1"

inFile = open('inputs/{}.in'.format(day), "r")

start_time = time.time()

print(sum(int(x) /3 -2 for x in inFile))
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))