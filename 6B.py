import time

day = "6B"

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


def orbitsBetween(start,target):
    current = start
    orbs = []
    while(target != current):
        for center, orbit in orbits.items():
            if(current in orbit):
                orbs.append(current)
                current = center
    return orbs


route = [j for sub in [orbitsBetween("YOU", "COM")[::-1],orbitsBetween("SAN", "COM")[::-1]] for j in sub]
print(len(set(route)) - (len(route) - len(set(route))) - 2)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))