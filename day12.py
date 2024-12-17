'''


'''
import sys
import copy
import itertools

borders = {}
areas = {}
cache =[]

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
            if col in areas.keys():
                areas[col].append((y,x))
            else:
                areas[col] = [(y,x)]
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

def print_grid(data):
    for row in data:
        print(''.join(row))

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

def getAreas():
    new_areas={}
    area_ids = areas.keys()
    for i in area_ids:
        distinct_areas =[]
        y_range = []

        for c in areas[i]:
            y_range.append(c[0])
        y_range = getRanges(list(set(y_range)))
    
        for y in y_range:
            x_range = []
            for c in areas[i]:
                if c[0] >= y[0] and c[0] <= y[1]:
                    x_range.append(c[1])
            x_range = getRanges(list(set(x_range)))

            for x in x_range:
                distinct_areas.append([y,x])

        new_areas[i] = distinct_areas
    return new_areas

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
    return result

def main():
    global borders
    global areas
    global cache
    filename = getFilename()
    data = parseFile(filename)

    part1_result =part1(data)

    if 'test' not in filename:
        if part1_result <= 338681:
            part1_result = 'Incorrect: too low'
        elif part1_result >=1539588:
            part1_result = 'Incorrect: too high'
   
    print(part1_result)

    #part2_result = part2(data)
    #print(part2_result)

main()
