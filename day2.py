'''
The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing 
or gradually decreasing. 

So, a report only counts as safe if both of the following are true:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:
7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

In this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?


'''
import sys
import copy

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    if argc > 1:
        filename = 'test_input.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    reports = []
    for line in f:
        data = line.split(' ')
        data = [int(d) for d in data]
        reports.append(data)

    return reports

def part1(reports):
    result = 0
    
    for r in reports:
        valid = True
        max_len = len(r)-1
        if r[0] == r[max_len]:
            continue
        increasing = False if r[0] > r[max_len] else True
        
        for i in range(max_len):
            if r[i] == r[i+1]:
                valid = False
                break
            if increasing:
                if (r[i] >= r[i+1]):
                    valid = False
                    break
            else:
                if (r[i] <= r[i+1]):
                    valid = False
                    break
            diff = abs(r[i] - r[i+1])
            if diff < 1 or diff > 3:
                valid = False
                break
            

        if valid:
            #print (r)
            result = result +1 
        
    return result

def part2(reports):
    result = 0
    for r in reports:
        valid = p2_CheckReport(r)
        
        if valid == False:
            for i in range(len(r)):
                temp = copy.deepcopy(r)
                temp.pop(i)
                valid = p2_CheckReport(temp)
                if valid:
                    break
                temp = None
        if valid:
            result = result +1
        
    return result

def p2_CheckReport(r):
    max_len = len(r)-1
    if r[0] == r[max_len]:
        return False
    increasing = False if r[0] > r[max_len] else True
    
    for i in range(max_len):
        if r[i] == r[i+1]:
            return False
        if increasing:
            if (r[i] >= r[i+1]):
                return False
        else:
            if (r[i] <= r[i+1]):
                return False
        diff = abs(r[i] - r[i+1])
        if diff < 1 or diff > 3:
            return False
    return True
                  

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
