'''
'''
import sys

cache = {}

def getFilename():
    argc = len(sys.argv)
    filename = 'input.txt'
    if argc > 1:
        filename = 'test_input.txt'
    return filename

def parseFile(filename):
    f = open(filename, "r")

    data = f.read()

    data = data.split(' ')

    return data

def part1(data):
    
    i = 0
    while i < 25:
        new_list = []
        for stone in data:
            new_stone = ''
            if stone == '0':
                new_stone = '1'
            elif len(stone)%2 == 0:
                stone_len = int(len(stone)/2)
                new_stone = stone[:stone_len]
                new_list.append(new_stone)
                new_stone = str(int(stone[stone_len:]))
            else:
                new_stone = str(int(stone)*2024)
            new_list.append(new_stone)
        data = new_list
        
        i+=1

    return len(data)

def part2(data):
    i = 0
    while i < 75:
        print(i)
        new_list = []

        for stone in data:
            new_stone = ''
            if stone == 0:
                new_stone = 1
            elif len(str(stone))%2 == 0:
                try:
                    new_list.append(cache[stone][0])
                    new_stone= cache[stone][1]
                except:
                    str_stone = str(stone)
                    stone_len = int(len(str_stone)/2)
                    val_1 = int(str_stone[:stone_len])
                    val_2 = int(str_stone[stone_len:])
                    new_list.append(val_1)
                    new_stone = val_2
                    cache[stone]=[val_1,val_2]
            else:
                new_stone = stone*2024
            new_list.append(new_stone)
        data = new_list
        
        i+=1

    return len(data)

def main():
    global cache
    global entire_cache
 
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    data = [int(d) for d in data]
    part2_result = part2(data)
    
    print(part2_result)

main()
