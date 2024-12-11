'''


'''
import sys
import copy
import numpy as np

def getFilename():
    argc = len(sys.argv)
    filename = 'input_6.txt'
    if argc > 1:
        filename = 'test_input_6.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    rows = []
    for line in f:
        data = line.strip()
        rows.append(list(data))

    return rows

def findGuard(data):
    max_rows = len(data)
    max_cols = len(data[0])
    x = 0
    for y in range(max_rows):
        row = data[y]
        if '^' in row:
            x = row.index('^')
            break
    return y,x

def walkPath(row,i):
    curr = row[i]
    guard_exit = False
    while curr != '#':
        if row[i] != '*':
            row[i] = 'X'
        i+=1
        if i >= len(row):
            guard_exit = True
            return row, guard_exit
        else:
            curr = row[i]
    row[i-1] = '^'
    return row,guard_exit

def rotate_left(data):
    data = list(zip(*data[::-1]))
    data = [list(d) for d in data]
    data = list(zip(*data[::-1]))
    data = [list(d) for d in data]
    data = list(zip(*data[::-1]))
    data = [list(d) for d in data]
    return data

def part1(data):
    result = 0
    
    #rotate grid to the right 
    data = list(zip(*data[::-1]))
    data = [list(d) for d in data]
    guard_gone = False

    while guard_gone == False:
        row,col = findGuard(data)
        data[row],guard_gone = walkPath(data[row],col)
        data = rotate_left(data)

    for row in data:
        for x in row:
            if x == 'X':
                result += 1

    return result

def getPath(data):
    path_coords = []

    walk_dir = 'UP'
    row,col = findGuard(data)
    guard_gone = False

    max_rows = len(data)
    max_cols = len(data[0])

    while guard_gone == False:
        data[row][col] = 'X'
        
        #check next spot
        if walk_dir == 'UP':
            row = row-1
        elif walk_dir == 'RIGHT':
            col = col+1
        elif walk_dir == 'DOWN':
            row = row+1
        else:
            col = col-1
        
        if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
            guard_gone = True 
            break
        #check for collision and change direction 
        if data[row][col] == '#':
            if walk_dir == 'UP':
                row = row+1
                col = col+1
                walk_dir = 'RIGHT'
            elif walk_dir == 'RIGHT':
                col = col-1
                row = row+1
                walk_dir = 'DOWN'
            elif walk_dir == 'DOWN':
                row = row-1
                col = col -1 
                walk_dir = 'LEFT'
            else:
                col = col + 1
                row = row-1
                walk_dir = 'UP'
        if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
            guard_gone = True 
            break
    for y,row in enumerate(data):
        for x,col in enumerate(row):
            if col == 'X':
                path_coords.append((y,x))
    return path_coords

def checkForLoop(data,row,col):
    walk_dir = 'UP'

    max_rows = len(data)
    max_cols = len(data[0])

    visited = {}

    max_loops = 100000
    loop_count = 0

    while loop_count < max_loops:
        #check next spot
        loop_count+=1

        prev = (row,col)
        if walk_dir == 'UP':
            row = row-1
        elif walk_dir == 'RIGHT':
            col = col+1
        elif walk_dir == 'DOWN':
            row = row+1
        else:
            col = col-1
        
        if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
            return False
        #check for collision and change direction 
        if data[row][col] == '#':
            if prev in visited.keys():
                if walk_dir in visited[prev]:
                    return True
                else:
                    visited[prev].append(walk_dir)
            else:
                visited[prev]=[walk_dir]

            if walk_dir == 'UP':
                row = row+1
                walk_dir = 'RIGHT'
            elif walk_dir == 'RIGHT':
                col = col-1
                walk_dir = 'DOWN'
            elif walk_dir == 'DOWN':
                row = row-1
                walk_dir = 'LEFT'
            else:
                col = col + 1
                walk_dir = 'UP'
        
        if row < 0 or row >= max_rows or col < 0 or col >= max_cols:
            return False
    return True

def part2(data):
    result = 0
    
    #get initial guard position
    row,col = findGuard(data)
    path_coords = getPath(copy.deepcopy(data))

    for coord in path_coords:
        temp = copy.deepcopy(data)
        temp[coord[0]][coord[1]] = '#'

        if checkForLoop(temp,row,col):
            result+=1
    
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    if part2_result >= 2358:
        part2_result = 'incorrect: too high'
    print(part2_result)

main()
