'''


'''
import sys

dirs = {
    '^':(-1,0),
    'v':(1,0),
    '<':(0,-1),
    '>':(0,1)
}

def getFilename():
    argc = len(sys.argv)
    filename = 'input_15.txt'
    if argc > 1:
        filename = 'test_input_15.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    data = f.read()

    data = data.split('\n\n')
    grid = data[0].split('\n')
    grid = [list(x) for x in grid]
    moves = list(data[1].replace('\n',''))
    
    return grid,moves

def parseFile2(filename):
    f = open(filename, "r")

    data = f.read()

    data = data.split('\n\n')

    data[0]=data[0].replace('#','##').replace('O','[]').replace('.','..').replace('@','@.')

    grid = data[0].split('\n')
    grid = [list(x) for x in grid]
    moves = list(data[1].replace('\n',''))
    
    return grid,moves

def findGuard(data):
    max_rows = len(data)
    max_cols = len(data[0])
    x = 0
    for y in range(max_rows):
        row = data[y]
        if '@' in row:
            x = row.index('@')
            break
    return (y,x)

def moveBoxes(val,row,col,grid,dir):
    if grid[row][col]=='#':
        return grid,False
    elif grid[row][col]=='O':
        grid,moved = moveBoxes('O',row+dir[0],col+dir[1],grid,dir)
        if moved:
            grid[row][col]=val
        return grid,moved
    else:
        grid[row][col]=val
        return grid,True

def moveBoxes2(val,row,col,grid,dir):
    if grid[row][col]=='#':
        return grid,False
    elif grid[row][col]=='[' or grid[row][col]==']':
        grid,moved = moveBoxes(grid[row][col],row+dir[0],col+dir[1],grid,dir)
        if moved:
            grid[row][col]=val
        return grid,moved
    else:
        grid[row][col]=val
        return grid,True

def part1(grid,moves):
    result = 0
    guard_pos = findGuard(grid)

    for m in moves:
        m = dirs[m]
        new_pos = (guard_pos[0]+m[0],guard_pos[1]+m[1])
        if grid[new_pos[0]][new_pos[1]] == '.':
            grid[guard_pos[0]][guard_pos[1]] = '.'
            grid[new_pos[0]][new_pos[1]] = '@'
            guard_pos = new_pos
        elif grid[new_pos[0]][new_pos[1]] == '#':
            continue
        else:
            grid,moved = moveBoxes('@',new_pos[0],new_pos[1],grid,m)
            if moved:
                grid[guard_pos[0]][guard_pos[1]] = '.'
                guard_pos = new_pos
    
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == 'O':
                gps = (100*y)+x
                result += gps


        
    
    return result

def part2(grid,moves):
    result = 0
    guard_pos = findGuard(grid)


    for m in moves:
        m = dirs[m]
        new_pos = (guard_pos[0]+m[0],guard_pos[1]+m[1])
        if grid[new_pos[0]][new_pos[1]] == '.':
            grid[guard_pos[0]][guard_pos[1]] = '.'
            grid[new_pos[0]][new_pos[1]] = '@'
            guard_pos = new_pos
        elif grid[new_pos[0]][new_pos[1]] == '#':
            continue
        else:
            if m[0]==0:
                grid,moved = moveBoxes2('@',new_pos[0],new_pos[1],grid,m)
                if moved:
                    grid[guard_pos[0]][guard_pos[1]] = '.'
                    guard_pos = new_pos
            else:
                break
    for row in grid:
        print(''.join(row))
    for y,row in enumerate(grid):
        for x,col in enumerate(row):
            if col == 'O':
                gps = (100*y)+x
                result += gps

    return result

def main():
    filename = getFilename()
    data,moves = parseFile2(filename)

    #part1_result =part1(data,moves)
    ##print(part1_result)

    
    part2_result = part2(data,moves)
    print(part2_result)

main()
