'''


'''
import sys
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
        row[i] = 'X'
        i+=1
        if i >= len(row):
            guard_exit = True
            return row, guard_exit
        else:
            curr = row[i]
    row[i-1] = '^'
    return row,guard_exit

def walkPath2(row,i):
    row[i] = '+'
    curr = row[i]
    loop_achieved = False
    while curr != '#':
        i+=1
        if i >= len(row):
            guard_exit = True
            return row, guard_exit
        else:
            curr = row[i]
    if row[i-1] == '+':
        loop_achieved = True
    row[i-1] = '^'
    return row,guard_exit
def printGrid(data):
    for row in data:
        row_str = ''.join(row)
        print(row_str+"\n")

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

def part2(data):
    result = 0
    
    #rotate grid to the right 
    data = list(zip(*data[::-1]))
    data = [list(d) for d in data]
    guard_gone = False
    firstPos = True

    while guard_gone == False:
        row,col = findGuard(data)
        data[row],guard_gone = walkPath2(data[row],col)
        if firstPos: 
            data[row][col] = 'X'
            firstPos = False
        data = rotate_left(data)
    printGrid(data)
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
