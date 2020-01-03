import time

day = "8"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

n = 25 * 6

lines = []

for line in inFile:
    line = line.strip('\n')
    lines = [line[i:i+n] for i in range(0, len(line), n)]

section = lines[0]

for line in lines: 
    if(line.count("0") < section.count("0")):
        section = line

print(section.count("1") * section.count("2"))
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))