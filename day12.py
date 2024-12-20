'''


'''
import sys
import copy
from queue import Queue

borders = {}
cache =[]

def bfs(maze, start, end):
    queue = Queue()
    queue.put([start])  # Enqueue the start position

    while not queue.empty():
        path = queue.get()  # Dequeue the path
        x, y = path[-1]     # Current position is the last element of the path

        if (x, y) == end:
            return path  # Return the path if end is reached

        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:  # Possible movements
            next_x, next_y = x + dx, y + dy
            if maze[next_x][next_y] != '#' and (next_x, next_y) not in path:
                new_path = list(path)
                new_path.append((next_x, next_y))
                queue.put(new_path)  # Enqueue the new path


def getFilename():
    argc = len(sys.argv)
    filename = 'input_12.txt'
    if argc > 1:
        filename = 'test_input_12.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    rows = []
    for line in f:
        data = list(line.strip())
        rows.append(data)

    return rows

def get_perimeters(data):
    perimiter = []
    for y,row in enumerate(data):
        new_row = []
        for x,col in enumerate(row):
            if y != 0 and y!= len(data)-1 and x != 0 and x!= len(row)-1 and data[y-1][x] == col and data[y+1][x] == col and data[y][x-1] == col and data[y][x+1] == col:
                new_row.append('.')
                borders[(y,x)]=0
            else:
                new_row.append(col)
                touch_points = 4
                if y != 0: 
                    touch_points = touch_points-(1 if data[y-1][x] == col else 0)
                if y!= len(data)-1:
                    touch_points = touch_points-(1 if data[y+1][x] == col else 0)
                if x != 0:
                    touch_points = touch_points-(1 if data[y][x-1] == col else 0)
                if x!= len(row)-1:
                    touch_points = touch_points-(1 if data[y][x+1] == col else 0)
                borders[(y,x)]=touch_points
        perimiter.append(new_row)

    return perimiter

def fillArea(data,row,col,val):
    filled =[]
    if data[row][col] != val:
        return filled
    
    if (row,col)in cache:
        return filled
    else:
        filled.append((row,col))
        cache.append((row,col))
    
    
    iterations = [(0,1),(1,0),(0,-1),(-1,0)]

    for iter in iterations:
        try:
            res= fillArea(data,row+iter[0],col+iter[1],val)
            if len(res) > 0:
                filled = filled + res
        except:
            continue
    
    
    return filled

def groupAreas(data):
    area_groups =[]

    for y,row in enumerate(data):
        for x,col in enumerate(row):
            new_area = []
            new_area = fillArea(data,y,x,col)
            if len(new_area) > 0:
                area_groups.append(new_area)

    return area_groups

def getRanges(data):
    s = e = None
    r = []
    for i in sorted(data):
        if s is None:
            s = e = i
        elif i == e or i == e + 1:
            e = i
        else:
            r.append((s, e))
            s = e = i
    if s is not None:
        r.append((s, e))
    return r

def part1(data):
    result = 0
    
    
    perimeter= get_perimeters(copy.deepcopy(data))
    distinct_areas = groupAreas(data)

    for a in distinct_areas:
        area_sum = len(a)
        perim_sum = 0
        for i in a:
            perim_sum = perim_sum+borders[(i[0],i[1])]
        result = result + (area_sum * perim_sum)
    return result

def part2(data):
    result = 0
    perimeter= get_perimeters(copy.deepcopy(data))
    distinct_areas = groupAreas(data)

    for a in distinct_areas:
        a.sort()
        rows = list(set([i[0] for i in a]))
        cols = list(set([j[1] for j in a]))
        
        for r in rows:
            r_cols = []
            r_cols = [x[1] if x[0] == r else -1 for x in a]
            r_cols = list(set([y if y != -1 else max(r_cols) for y in r_cols]))
            r_cols.sort()

            r_range=getRanges(r_cols)
            print(len(r_range))
        for c in cols:
            c_rows = []
            c_rows = [x[0] if x[1] == c else -1 for x in a]
            c_rows  = list(set([y if y != -1 else max(c_rows ) for y in c_rows ]))
            c_rows.sort()

            c_range=getRanges(c_rows)
            print(len(c_range))
        print('==========')


        area_sum = len(a)
        side_sum = 0

        result = result + (area_sum * side_sum)
    return result

def main():
    global borders
    global areas
    global cache
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
