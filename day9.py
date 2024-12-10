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
    
def generateDiscImage2(data):
    index = 0
    file_id = -1
    disc = []

    while index < len(data):
        if index%2== 0:
            file_id+=1
            id = file_id
        else:
            id = 'Space'

        disc.append({'id':id,'count':int(data[index])})
        index+=1
    return disc

def generateDiscImage3(data):
    index = 0
    disc = []
    for d in data:
        if d["id"]== 'Space':
            insert = '.'
        else:
            insert = d["id"]
            
        for i in range(d["count"]):
            disc.append(insert)
        index+=1
    return disc
    
def formatDisc(disc):
    file_ids = [x["id"] for x in disc if x["id"] != "Space"]

    for i in file_ids[::-1]:
        disc_len=len(disc)-1
        for d_index,d in enumerate(disc[::-1]):
            if d["id"] == i:
                disc_index = disc_len - d_index
                break
        for d_index in range(disc_index):
            d = disc[d_index]
            if d["id"] == 'Space' and d['count'] >= disc[disc_index]['count']:
                disc[d_index]['count']=d['count']-disc[disc_index]['count']
                temp = {
                    'id':i,
                    'count':disc[disc_index]['count']
                }
                disc[disc_index]["id"] = 'Space'
                disc.insert(d_index,temp)
                break
            else:
                continue
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
    disc = generateDiscImage2(data)
    disc = formatDisc(disc)
    disc = generateDiscImage3(disc)

    for i in range(len(disc)):
        if disc[i] == '.':
            continue
        result = result + (i*disc[i])
    return result

def main():
    filename = getFilename()
    data = parseFile(filename)

    #part1_result =part1(data)
    #print(part1_result)

    part2_result = part2(data)
    print(part2_result)

main()
