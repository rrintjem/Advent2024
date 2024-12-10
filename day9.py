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


    return list(data.strip())

def generateDiscImage(data):
    index = 0
    file_id = -1
    disc = []
    while index < len(data):
        if index%2== 0:
            file_id+=1
            insert = file_id
        else:
            insert = '.'
        for i in range(int(data[index])):
            disc.append(insert)
        index+=1
    return disc
    
def part1(data):
    result = 0

    disc = generateDiscImage(data)

    indices = [i for i, x in enumerate(disc) if x == "."]

    disc_len=len(disc)-1
    for i in indices:
        while disc[disc_len] == '.':
            disc_len = disc_len-1
        if disc_len <= i:
            break
        disc[i]=disc[disc_len]
        disc[disc_len] = '.'
    
    for i in range(len(disc)):
        if disc[i] == '.':
            break
        result = result + (i*disc[i])


    
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
