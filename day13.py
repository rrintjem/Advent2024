'''


'''
import re
import sys
import numpy as np
from sympy import symbols, Eq, solve

A_COST= 3
B_COST = 1

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    if argc > 1:
        filename = 'test_input.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    data = f.read()

    '''
    {
        a: (x,y)
        b:(x,y)
        prize: (x,y)
    }


    '''

    data = data.split('\n\n')
    new_data=[]
    for d in data:
        a = re.findall(r'Button A: X\+(\d*), Y\+(\d+)',d)[0]
        b = re.findall(r'Button B: X\+(\d*), Y\+(\d+)',d)[0]
        p = re.findall(r'Prize: X\=(\d*), Y\=(\d+)',d)[0]
        parsed_data={
            'a':(int(a[0]),int(a[1])),
            'b':(int(b[0]),int(b[1])),
            'p':(int(p[0]),int(p[1]))
        }
        new_data.append(parsed_data)

        

    return new_data

def part1(data):
    result = 0
    x, y = symbols('x y')

    for d in data:
        '''
        x*a[0] + y*b[0] - p[0] 
        and x*a[1] + y*b[1] - p[1]
        '''
        
        eq1 = Eq((x*d['a'][0]) + (y*d['b'][0]), d['p'][0])
        eq2 = Eq((x*d['a'][1]) + (y*d['b'][1]), d['p'][1])
        solution = solve((eq1,eq2), (x, y))


        if '/' in str(solution[x]) or '/' in str(solution[y]):
            continue
        else:
            result = result + (A_COST*solution[x]) + (B_COST*solution[y])
       

    
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
