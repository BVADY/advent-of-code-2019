import numpy as np
import time

day = "8B"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

width = 25
height = 6
n = width * height


layers = []

for line in inFile:
    line = line.strip('\n')
    layers = [line[i:i+n] for i in range(0, len(line), n)]

raw = ["2"]*n

for i in range(0,n):
    for layer in layers:
        if(layer[i] != "2"):
            raw[i] = layer[i]
            break


image = [raw[i:i+width] for i in range(0, len(raw), width)]

print("")
for layer in image:
    for l in layer:
        if(l == "1"):
            print("*"),
        else: 
            print(" "),
    print("")
print("")
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))