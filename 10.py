import math
import time

day = "10"

inFile = open('inputs/{}.in'.format(day), "r")

start_time = time.time()

board = []

for line in inFile:
    line = line.strip("\n")
    row = []
    for item in line:
        if(item == '.'):
            row.append(0)
        else:
            row.append(1)
    board.append(row)


def calcSight(r,c):
    if(board[r][c] == 0):
        return 0

    angles = []
    for i in range(len(board)):
        for j in range(len(board)):
            if(board[i][j] == 1 and (i,j != r,c)):
                angles.append((math.atan2(r-i, c-j)))
    return len(set(angles)) 


result = [[0 for y in range(len(board[0]))] for x in range(len(board))]
for i in range(0,len(board)):
    for j in range(0,len(board[i])):
        result[i][j] = calcSight(i,j)

print(max(map(max, result)))
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))