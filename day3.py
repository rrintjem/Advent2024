'''


'''
import sys
import re

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    if argc > 1:
        filename = 'test_input.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    data = f.read()

    return data

def part1(data):
    result = 0
    calcs = re.findall(r'mul\(\d+,\d+\)', data)
    print (calcs)
    for c in calcs:
        vals = c.replace('mul(','').replace(')','').split(',')
        prod = int(vals[0])*int(vals[1])
        result += prod
    return result

def part2(data):
    result = 0
    calcs = re.findall(r'(mul\(\d+,\d+\))|(don\'t\(\))|(do\(\))', data)
  
    do = True
    for c in calcs:
        if c[0] == '':
            if c[1] == '':
                do = True
            else:
                do = False
        elif(do):
            vals = c[0].replace('mul(','').replace(')','').split(',')
            prod = int(vals[0])*int(vals[1])
            result += prod

    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
