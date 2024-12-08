'''


'''
import sys
import copy
import itertools
from numpy import ones,vstack
from numpy.linalg import lstsq

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    if argc > 1:
        filename = 'test_input.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    rows = []
    for line in f:
        data = line.strip()
        data = [d for d in data]
        rows.append(data)

    return rows

def getSignalCoords(data):
    coords = {}
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] != '.':
                if data[row][col] in coords.keys():
                    coords[data[row][col]].append((row,col))
                else:
                    coords[data[row][col]] = [(row,col)]
    return coords

def getSignalLines(coords):
    res = []

    res = [list(i) for i in itertools.combinations(coords,2)]

    nodes = []

    for r in res:
        
        x_coords, y_coords = zip(*r)
        A = vstack([x_coords,ones(len(x_coords))]).T
        m, c = lstsq(A, y_coords)[0]

        if(x_coords[0]>x_coords[1]):
            diff = x_coords[0]-x_coords[1]
            node_x = (x_coords[0]+diff,x_coords[1]-diff)
        else:
            diff = x_coords[1]-x_coords[0]
            node_x = (x_coords[1]+diff,x_coords[0]-diff)
        node_y = (round((node_x[0]*m)+c),round((node_x[1]*m)+c))

        nodes.append((node_x[0],node_y[0]))
        nodes.append((node_x[1],node_y[1]))

        #print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

    return nodes

def getSignalLines2(coords,x_max):
    res = []

    res = [list(i) for i in itertools.combinations(coords,2)]

    nodes = []

    for r in res:
        
        x_coords, y_coords = zip(*r)
        A = vstack([x_coords,ones(len(x_coords))]).T
        m, c = lstsq(A, y_coords)[0]

        if(x_coords[0]>x_coords[1]):
            max_id = 0
            min_id = 1
        else:
            max_id = 1
            min_id = 0
        diff = x_coords[max_id]-x_coords[min_id]
        x = x_coords[max_id]
        while x < x_max:
            nodes.append((x,round((x*m)+c)))
            x = x + diff
        x = x_coords[min_id]
        while x >= 0:
            nodes.append((x,round((x*m)+c)))
            x = x - diff
        '''for x in range(x_coords[min_id]):
            nodes.append((x,round((x*m)+c)))
        for x in range(x_coords[max_id]+1,x_max):
            nodes.append((x,round((x*m)+c)))
        '''
        #print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

    return nodes

def part1(data):
    result = 0
    res_data = copy.deepcopy(data)

    y_max = len(data)
    x_max = len(data[0])

    coords = getSignalCoords(data)
    for key in coords.keys():
        nodes = getSignalLines(coords[key])
        for n in nodes:
            if n[0] >= 0 and n[0] < x_max and n[1] >= 0 and n[1] < y_max:
                res_data[n[0]][n[1]] = '#'
                

    for row in res_data:
        result+=row.count('#')
    

    
    return result

def part2(data):
    result = 0

    res_data = copy.deepcopy(data)

    y_max = len(data)
    x_max = len(data[0])

    coords = getSignalCoords(data)
    for key in coords.keys():
        nodes = getSignalLines2(coords[key],x_max)
        for n in nodes:
            if n[0] >= 0 and n[0] < x_max and n[1] >= 0 and n[1] < y_max:
                res_data[n[0]][n[1]] = '#'
                

    for row in res_data:
        #print(''.join(row))
        result+=row.count('#')
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result = part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
