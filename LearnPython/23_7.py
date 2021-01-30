col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

padding = [['.' for i in range(col+2)] for j in range(row+2)]

for i in range(1,row+1):
    for j in range(1,col+1):
        padding[i][j] = matrix[i-1][j-1]

mine = []

for i in range(1, row+1):
    mine.append([])
    for j in range(1, col+1):
        if padding[i][j] == '*': mine[i-1].append('*')
        else:

            count = 0
            if padding[i-1][j-1] == '*': count += 1 
            if padding[i-1][j] == '*': count += 1 
            if padding[i-1][j+1] == '*': count += 1 
            if padding[i][j-1] == '*': count += 1 
            if padding[i][j+1] == '*': count += 1
            if padding[i+1][j-1] == '*': count += 1 
            if padding[i+1][j] == '*': count += 1 
            if padding[i+1][j+1] == '*': count += 1 
            
            mine[i-1].append(count)

for i in range(row):
    for j in range(col):
        print(mine[i][j], end='')
    print()
