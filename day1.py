'''
This time, you'll need to figure out exactly how often each number 
from the left list appears in the right list. 

Calculate a total similarity score by adding up each number in the 
left list after multiplying it by the number of times that number appears in the right list.

The first number in the left list is 3. 
It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.

The second number in the left list is 4. 
It appears in the right list once, so the similarity score increases by 4 * 1 = 4.

The third number in the left list is 2. 
It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).

The fourth number, 1, also does not appear in the right list.

The fifth number, 3, appears in the right list three times; the similarity score increases by 9.

The last number, 3, appears in the right list three times; the similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this process is 
31 (9 + 4 + 0 + 0 + 9 + 9).
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

    col_1 = []
    col_2 = []
    for line in f:
        data = line.split('   ')
        col_1.append(int(data[0]))
        col_2.append(int(data[1]))

    col_1.sort()
    col_2.sort()
    return col_1,col_2

def part1(col_1,col_2):
    distances = 0
    for i in range(len(col_1)):
        diff = col_1[i] - col_2[i]
        distances= distances+abs(diff)
    return distances

def part2(col_1,col_2):
    col2_dict = {j:col_2.count(j) for j in col_2}
    c2_keys = col2_dict.keys()
    total = 0
    for i in col_1:
        val = i
        if i in c2_keys:
            val = val*col2_dict[i]
            total = total + val
    return total




def main():
    filename = getFilename()
    col_1,col_2 = parseFile(filename)

    part1_result =part1(col_1,col_2)
   

    part2_result = part2(col_1,col_2)
    print(part2_result)

main()
