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
    data = f.read()

    data = data.split('\n\n')

    return data

def create_rules(rules):
    rules_dict = {}

    for r in rules: 
        key1 = str(r[0])
        key2 = str(r[1])
        if key1 in rules_dict.keys():
            rules_dict[str(r[0])]["before"].append(r[1])
        else: 
            rules_dict[str(r[0])] = {
                "before":[r[1]],
                "after":[]
            }
        if key2 in rules_dict.keys():
            rules_dict[str(r[1])]["after"].append(r[0])
        else: 
            rules_dict[str(r[1])] = {
                "after":[r[0]],
                "before":[]
            }
    return rules_dict

def part1(data):
    result = 0
    rules = [[int(r) for r in d.split('|')]  for d in data[0].split('\n')]
    updates = [[int(u) for u in d.split(',')] for d in data[1].split('\n')] 

    #distinct_rules = [int(d) for d in list(dict.fromkeys(data[0].replace('\n','|').split('|')))]
    rules_dict = create_rules(rules)


    for row in updates:
        valid = True
        for i in row:
            num_rule = rules_dict[str(i)]
            for b in num_rule["before"]:
                if b not in row:
                    continue
                if row.index(b)<row.index(i):
                    valid = False
                    break
            if valid:
                for a in num_rule["after"]:
                    if a not in row:
                        continue
                    if row.index(a)>row.index(i):
                        valid = False
                        break
            if valid == False:
                break
        if valid:
            result = result + row[int((len(row)-1)/2)]

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
