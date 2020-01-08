import sys
import numpy as np 
import time

day = "3"

inFile = open('inputs/{}.in'.format(day), "r")

start_time = time.time()

lines = []
A = [[0,0]]
B = [[0,0]]

def draw(board, direction, distance, start_coor):
    distance = distance +1
    if(direction == "D"):
        for i in range(start_coor[1] -1 , start_coor[1] - distance, -1):
            board.append([start_coor[0], i])
    if(direction == "U"):
        for i in range(start_coor[1] +1, start_coor[1] + distance):
            board.append([start_coor[0], i])
    if(direction == "L"):
        for i in range(start_coor[0] -1, start_coor[0] - distance, -1):
            board.append([i, start_coor[1]])
    if(direction == "R"):
        for i in range(start_coor[0] +1, start_coor[0] + distance):
            board.append([i, start_coor[1]])

for line in inFile:
    line = line.strip('\n')
    lines.append(line.split(','))

for item in lines[0]:
        direction = item[0]
        distance = int(item.strip(direction))
        start_coor = A[-1]
        draw(A,direction, distance, start_coor)

for item in lines[1]:
        direction = item[0]
        distance = int(item.strip(direction))
        start_coor = B[-1]
        draw(B,direction, distance, start_coor)


A = map(tuple, A)
B = map(tuple, B)

intersections = set(A).intersection(set(B))
intersections.remove((0,0))

distance = sys.maxint

for inter in intersections:
    distance = min(distance, abs(inter[0]) + abs(inter[1]))

print(distance)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))