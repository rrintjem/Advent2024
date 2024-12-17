'''
'''
import re
import sys

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    grid = (103,101)
    if argc > 1:
        filename = 'test_input.txt'
        grid = (7,11)
    return filename,grid

def buildGrid(dim):
    grid = []
    x_axis = int((dim[1] - 1)/2)
    y_axis = int((dim[0] - 1)/2)
    for row in range(dim[0]):
        if row == y_axis:
            grid_row = [' ']*dim[1]
        else:
            grid_row = ['.']*dim[1]
            grid_row[x_axis] = ' '
        grid.append(grid_row)
    return grid
        
def parseFile(filename):
    f = open(filename, "r")

    rows = []
    for line in f:
        #p=0,4 v=3,-3
        line = line.split(' ')
        p = line[0].replace('p=','').split(',')
        v = line[1].replace('v=','').split(',')
        data = {
            'p':(int(p[0]),int(p[1])),
            'v':(int(v[0]),int(v[1]))
        }
        rows.append(data)

    return rows
def part1(data,dim):
    result = 1
    max_x = dim[1]
    max_y = dim[0]
    grid = buildGrid(dim)
    q_sums = [0,0,0,0]
    x_axis = int((dim[1] - 1)/2)
    y_axis = int((dim[0] - 1)/2)
    

    for robot in data:
        for i in range(100):
            y = robot['p'][1]
            x = robot['p'][0]

            new_y = y+robot['v'][1]
            new_x = x+robot['v'][0]

            if new_x < 0:
                new_x = max_x+new_x
            elif new_x >= max_x:
                new_x = new_x - max_x
            if new_y < 0:
                new_y = max_y+new_y
            elif new_y >= max_y:
                new_y = new_y - max_y
            robot['p'] = (new_x,new_y)
        if grid[robot['p'][1]][robot['p'][0]] == ' ':
            continue

        if robot['p'][1] < y_axis:
            if robot['p'][0] < x_axis:
                q_sums[0]+=1
            else:
                q_sums[1]+=1
        else:
            if robot['p'][0] < x_axis:
                q_sums[2]+=1
            else:
                q_sums[3]+=1
        if grid[robot['p'][1]][robot['p'][0]] == '.':
            grid[robot['p'][1]][robot['p'][0]] = '1'
        else:
            grid[robot['p'][1]][robot['p'][0]]= str(int(grid[robot['p'][1]][robot['p'][0]])+1)

    
    result = q_sums[0]*q_sums[1]*q_sums[2]*q_sums[3]
    return result

def part2(data):
    result = 0
    return result


def main():
    filename,dim = getFilename()
    data = parseFile(filename)
    

    part1_result =part1(data,dim)
    print(part1_result)

    #part2_result = part2(data)
    #print(part2_result)

main()
