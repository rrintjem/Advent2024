'''


'''
import sys
import itertools

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
        data = line.split(':')
        data[0] = int(data[0])
        data[1] = data[1].strip()#.split(' ')
        rows.append(data)

    return rows

def getOperatorCombos(eqn):
    num_operators = eqn.count(' ')

    start_str = '+'*num_operators
    res = []

    for sub in itertools.product((True, False), repeat = len(start_str)):
        res.append("".join(chr if ele else '*' for chr, ele in zip(start_str, sub)))
    

    return res
    
def calculate(num1,num2,operator):
    if operator == '+':
        return num1 + num2
    else:
        return num1 * num2

def part1(data):
    result = 0
    for row in data:
       # print(row)
        indexes = [i for i, ltr in enumerate(row[1]) if ltr == ' ']
        combos = getOperatorCombos(row[1])
        num_operators = row[1].count(' ')

        row_list = [int(d) for d in row[1].split(' ')] 

        
        for c in combos:
            c = list(c)
            row_calc = row_list[0]
            for index in range(1,len(row_list)):
                row_calc = calculate(row_calc,row_list[index],c[index-1])
            # print('     '+str(row_calc)+" = "+str(row_list)+" "+str(c))
            if row_calc == row[0]:
                result = result + row[0]
                break

        '''
        for c in combos: 
            c = list(c)
            list_str = list(row[1])
            for i in range(num_operators):
                list_str[indexes[i]] = c[i]
            ans = eval(''.join(list_str))

            print('     '+str(ans)+" = "+''.join(list_str))
            if ans == row[0]:
                result = result + row[0]
                break
        '''
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
