import time

day = "2B"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

start = []
board = []
desired = 19690720


def opcode(item):
    if(item[0] == 1):
        board[item[3]] = board[item[1]] +  board[item[2]]
            
    if(item[0] == 2):
        board[item[3]] = board[item[1]] *  board[item[2]]


def intcode(a,b):
    j = 0
    board[1] = a
    board[2] = b
    while(j < len(board)-4):
        line = []
        for i in range(j, j+4):
            line.append(board[i])
        opcode(line)
        j += 4

    if(board[0] == desired):
        print('{}{}'.format(board[1], board[2]))
        print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))
        exit()


for line in inFile:
    start = line.split(',')

permutations = [[k,l] for k in range(0,100)
            for l in range(0,100)]


for perm in permutations:
    board = map(int, start)
    board[1] = 12
    board[2] = 2
    intcode(perm[0],perm[1])