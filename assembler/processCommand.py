import dictionaries

def dest2bin(mnemonic):
    # returns the binary code for the dest part of a C-instruction
    # sort the mnemonic to overcome destinations like AD, which is 
    # the same as DA. This is probably easier to do by adding more
    # entries in the dictionary
    return dictionaries.dest_dictionary.get(mnemonic, '000')         #ex. enter AM and get 101

def comp2bin(mnemonic):
    # returns the binary code for the comp part of a C-instruction
    return dictionaries.comp_dictionary.get(mnemonic, '0000000') 

def jump2bin(mnemonic):
    # returns the binary code for the jump part of a C-instruction
    return dictionaries.jump_dictionary.get(mnemonic, '000') 
    
def commandType(command):
    # returns "A_COMMAND", "C_COMMAND", or "L_COMMAND"
    # depending on the contents of the 'command' string
    if (command[0] == '@'):
        ans = "A_COMMAND"
    
    elif (command[0] == "(" and ")" in command): #maybe add ) condition
        ans = "L_COMMAND"
    
    else:
        if ("=" in command or ";" in command):
            ans = "C_COMMAND"
        else:
            return "error_unidintifiable command"
    
    return ans

def getSymbol(command):
    # given an A_COMMAND or L_COMMAND type, returns the symbol as a string,
    # eg (XXX) returns 'XXX'
    # @sum returns 'sum'
    if (command[0] == "(" and ")" in command): #maybe fix this in future
        command = command.replace("(", "")
        command = command.replace(")", "")

    elif (command[0] == "@"):
        return command[1:]

    else:
        return "error"
    
    return command

def getDest(command):
    # return the dest mnemonic in the C-instruction 'commmand'
    if "=" in command:
        lhs, rhs = command.split("=")
        return lhs
    
    else:
        return "null"
    
def getComp(command):
    # return the comp mnemonic in the C-instruction 'commmand'
    # lhs=rhs;jhs

    #check for equal first
    if "=" in command:
        lhs, rhs = command.split("=")

    else:
        rhs = command

    #now check for semicolon
    if ";" in rhs:
        jhs, unused = rhs.split(";")
        return jhs
    
    else:
        return rhs
   
def getJump(command):
    # return the jump mnemonic in the C-instruction 'commmand'
    if ";" in command:
        lhs, rhs = command.split(";")
        return rhs
    
    else:
        return "null"
    
def processA(line):
    # Convert an A-instruction line of assmebly to a binary code that is
    # 0 followed by a 15 bit address. Will use the symbol table to lookup
    # a symbol and replace it with a value. If label is not is symbol table
    # add it with correct RAM address (next in sequence)
    symbol = getSymbol(line)
    if symbol.isdigit():
        address = int(symbol)
    else:
        if symbol not in dictionaries.symbol_dictionary:
            dictionaries.symbol_dictionary[symbol] = format(16 + len(dictionaries.symbol_dictionary) - 23, '016b')
        address = int(dictionaries.symbol_dictionary[symbol], 2)

    return '0' + format(address, '015b')


def processC(line):
    # Convert a C-instruction line of code to the correct computation, destination,
    # and jump binary codes. These should be preceded by 111, which signifies the
    # C-instruction
    dest = getDest(line)
    comp = getComp(line)
    jump = getJump(line)

    return '111' + comp2bin(comp) + dest2bin(dest) + jump2bin(jump)

def processL(line,lineNo):
    # When an L-Instruction (label in the form (LABEL)) is encountered, 
    # the label should be placed into the symbol table with the correct line
    symbol = getSymbol(line)
    
    if symbol not in dictionaries.symbol_dictionary:
        dictionaries.symbol_dictionary[symbol] = format(lineNo, '016b')    