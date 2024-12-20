'''

The computer knows eight instructions, each identified by a 3-bit number (called the instruction's opcode). 
Each instruction also reads the 3-bit number after it as an input; this is called its operand.
A number called the instruction pointer identifies the position in the program from which the next opcode will be read; 
it starts at 0, pointing at the first 3-bit number in the program. 

Except for jump instructions, the instruction pointer increases by 2 after each instruction is processed 
(to move past the instruction's opcode and its operand). 
'''
import sys

REG_A = 0
REG_B = 0
REG_C = 0

OUTPUT = ''

def getData():
    global REG_A
    argc = len(sys.argv)
    
    if argc > 1:
        commands  = [(0,1),
                     (5,4),
                     (3,0)]
        REG_A = 729
    else:
        REG_A = 51571418
        commands = [(2,4),
                (1,1),
                (7,5),
                (0,3),
                (1,4),
                (4,5),
                (5,5),
                (3,0)]
    return commands 

def getComboOperand(operand):
    '''Combo operands 0 through 3 represent literal values 0 through 3.
    Combo operand 4 represents the value of register A.
    Combo operand 5 represents the value of register B.
    Combo operand 6 represents the value of register C.
    Combo operand 7 is reserved and will not appear in valid programs.'''
    if operand <= 3:
        return operand
    if operand == 4:
        return REG_A
    if operand == 5:
        return REG_B
    if operand == 6:
        return REG_C
    return None

def opCode0(operand):
    global REG_A
    '''The adv instruction (opcode 0) performs division. 
    The numerator is the value in the A register. 
    The denominator is found by raising 2 to the power of the instruction's combo operand. 
        (So, an operand of 2 would divide A by 4 (2^2); 
        an operand of 5 would divide A by 2^B.) 
    The result of the division operation is truncated to an integer and then written to the A register.
    '''
    operand = getComboOperand(operand)
    numerator = REG_A
    denominator = 2**operand

    REG_A = int(numerator/denominator)

    return 1

def opCode1(operand):
    global REG_B
    '''The bxl instruction (opcode 1) calculates the bitwise XOR of register B 
    and the instruction's literal operand, then stores the result in register B.
    '''

    REG_B = REG_B ^ operand
    return 1

def opCode2(operand):
    global REG_B
    '''The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 
    (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    '''
    operand = getComboOperand(operand)
    REG_B = operand % 8
    return 1

def opCode3(operand):
    global REG_A
    '''The jnz instruction (opcode 3) does nothing if the A register is 0. 
    However, if the A register is not zero, it jumps by setting the instruction 
    pointer to the value of its literal operand; 
    
    if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    '''
    if REG_A == 0:
        return 1
    return int(operand/2)

def opCode4(operand):
    global REG_B
    global REG_C
    '''The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, 
    then stores the result in register B. 
    (For legacy reasons, this instruction reads an operand but ignores it.)

    '''
    REG_B = REG_B^REG_C
    return 1

def opCode5(operand):
    global OUTPUT
    '''The out instruction (opcode 5) calculates the value of its combo operand modulo 8, 
    then outputs that value. (If a program outputs multiple values, they are separated by commas.)

    '''
    operand = getComboOperand(operand)
    OUTPUT = OUTPUT+str(operand % 8)+','
    return 1 

def opCode6(operand):
    global REG_A
    global REG_B
    '''The bdv instruction (opcode 6) works exactly like the
      adv instruction except that the result is stored in the B register. 
    (The numerator is still read from the A register.)
    '''
    operand = getComboOperand(operand)
    numerator = REG_A
    denominator = 2**operand

    REG_B = int(numerator/denominator)
    return 1

def opCode7(operand):
    global REG_A
    global REG_C
    '''The cdv instruction (opcode 7) works exactly like the adv instruction except 
    that the result is stored in the C register. 
    (The numerator is still read from the A register.)

    '''
    operand = getComboOperand(operand)
    numerator = REG_A
    denominator = 2**operand

    REG_C = int(numerator/denominator)
    return 1

def part1(data):
    result = 0

    i = 0
    while i < len(data):
        fn = 'opCode'+str(data[i][0])
        res = eval('%s(%s)'%(fn,data[i][1]))
        if res == 0:
            i = res
        else:
            i+= res 
    
    result = OUTPUT
    return result

def part2(data):
    result = 0
    return result

def main():
    global REG_A
    global REG_B
    global REG_C
    data = getData()

    part1_result =part1(data)
    print(part1_result)

    #part2_result = part2(data)
    #print(part2_result)

main()
