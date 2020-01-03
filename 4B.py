import time

day = "4B"

inFile = open('{}.in'.format(day), "r")

start_time = time.time()

BEGIN = 0
END = 0

for line in inFile:
  BEGIN = int(line.split("-")[0])
  END = int(line.split("-")[1])


def isValidPassword(password):
    pwd = str(password)
    if(len(pwd) != 6):
        return False
        
    last = 10
    for i in range(len(pwd) -1, -1, -1):
        if(int(pwd[i]) > last):
            return False
        
        last = int(pwd[i])

    if(len(pwd) == len(set(pwd))):
        return False

    for i in range(1,10):
        x = (len(pwd) - len(pwd.translate(None, str(i))))
        if(x / 2.0 == 1): 
            return True
            
    return False


count = 0    

for i in range(BEGIN, END):
    if(isValidPassword(i)):
        count = count +1

print(count)
print('Execution time: {} ms'.format(round((time.time() - start_time)*1000, 1)))