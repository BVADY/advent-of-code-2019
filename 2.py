import time

day = '2'

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

board = []


def opcode(item):
    if(item[0] == 1):
        board[item[3]] = board[item[1]] +  board[item[2]]
            
    if(item[0] == 2):
        board[item[3]] = board[item[1]] *  board[item[2]]
        
    if(item[0] == 99):
        print(str(board[0]))
        print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))
        exit()
    

def intcode():
    j = 0
    while(True):
        line = []
        for i in range(j, j+4):
            line.append(board[i])
        opcode(line)
        j += 4


for line in inFile:
    board = line.split(',')

board[1] = 12
board[2] = 2
board = map(int, board)
intcode()