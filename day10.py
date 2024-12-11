'''


'''
import sys

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
        data = list(line.strip())
        data = [int(d) for d in data]
        rows.append(data)

    return rows

def countTrails(data,row,col,val,trails):

    total = 0
    if val == 9:
        for t in trails:
            if t[0] == row and t[1] == col:
                return 0,trails
        trails.append((row,col))
        return 1,trails

    #check Up
    if row > 0 and data[row-1][col] == val+1 :
        res,trails =countTrails(data,row-1,col,val+1,trails)
        total = total+ res
    #check Down
    if row < len(data)-1 and data[row+1][col] == val+1 :
        res,trails =countTrails(data,row+1,col,val+1,trails)
        total = total+ res
    #check Left
    if col > 0 and data[row][col-1] == val+1 :
        res,trails =countTrails(data,row,col-1,val+1,trails)
        total = total+ res
    #check Right
    if col < len(data[0])-1 and data[row][col+1] == val+1 :
        res,trails =countTrails(data,row,col+1,val+1,trails)
        total = total+ res
    
    
    return total,trails

def part1(data):
    result = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == 0:
                trails = []
                res = 0
                res,_ = countTrails(data,row,col,data[row][col],trails)
                result +=res

    return result

def part2(data):
    result = 0
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    part1_result =part1(data)
    print(part1_result)

    #part2_result = part2(data)
    #print(part2_result)

main()
