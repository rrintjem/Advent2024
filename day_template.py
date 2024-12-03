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

    data = f.read()

    reports = []
    for line in f:
        data = line.split(' ')
        data = [int(d) for d in data]
        reports.append(data)

    return reports

def part1(data):
    result = 0
    
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
