import time

day = "6"

inFile = open('inputs/{}.in'.format(day), "r")

start_time = time.time()

orbits = {}

for line in inFile:
    line = line.strip('\n')
    center = line.split(")")[0]
    satelite = line.split(")")[1]
    if(center in orbits):
        orbits[center].append(satelite)
    else:
        orbits[center] = [satelite]


def calcDistance(startOrbit,target):
    current = startOrbit
    distance = 0
    while(target != current):
        for center, orbit in orbits.items():
            if(current in orbit):
                distance = distance + 1
                current = center
    return distance

result = 0
for key, value in orbits.items():
    for orbit in value: 
        result = result + calcDistance(orbit,"COM")


print(result)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))