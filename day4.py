'''


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

    rows = []
    for line in f:
        data = list(line.strip())
        rows.append(data)

    return rows

def formatArrays(data):
    data_vertical = copy.deepcopy(data)
    data_vertical = list(zip(*data_vertical[::-1]))

    data_diag_1 = copy.deepcopy(data)
    data_diag_2 = copy.deepcopy(data_vertical)

    data_diag_1  =  rotate_array(data_diag_1)
    data_diag_2  =  rotate_array(data_diag_2)

    data = data + data_vertical + data_diag_1 + data_diag_2

    return [''.join(str(x) for x in d) for d in data]
 
def rotate_array(mat):
    rows = len(mat)
    cols = len(mat[0])
    diags = [[mat[sum_-k][k]
          for k in range(sum_ + 1)
          if (sum_ - k) < rows and k < cols]
         for sum_ in range(rows + cols - 1)]
    return diags

def part1(data):
    result = 0
    data = formatArrays(data)

    for s in data:
        if len(s) < 4:
            continue
        result =  result + s.count('XMAS')
        result =  result + s.count('SAMX')   
    return result

def part2(data):
    result = 0
    max_rows=len(data)
    max_cols=len(data[0])
    for row in range(1,(max_rows-1)):
        for col in range(1,(max_cols-1)):
            if data[row][col] == 'A':
                d_1 = data[row-1][col-1]+data[row][col]+data[row+1][col+1]
                d_2 = data[row+1][col-1]+data[row][col]+data[row-1][col+1]
                if (d_1 == 'MAS' or d_1 == 'SAM') and (d_2 == 'MAS' or d_2 == 'SAM'):
                    result+=1
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)
    
    part2_result = part2(data)
    print(part2_result)

main()
