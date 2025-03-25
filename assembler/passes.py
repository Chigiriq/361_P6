import processCommand

def pass_1(file):
    # scan each line of file and find L_COMMANDS
    # place them in the symbol table with appropriate ROM numbers
    rom_address = 0
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('//'):
                continue

            line = line.split('//')[0].strip()

            if processCommand.commandType(line) == "L_COMMAND":
                processCommand.processL(line, rom_address)

            else:
                rom_address += 1
                

def pass_2(input_file, output_file):
    # Scan file and write correct binary code to file.
    with open(input_file, 'r') as f, open(output_file, 'w') as out:
        for line in f:
            line = line.strip()

            if not line or line.startswith('//'):
                continue

            line = line.split('//')[0].strip()

            if processCommand.commandType(line) == "A_COMMAND":
                binary = processCommand.processA(line, 0)

            elif processCommand.commandType(line) == "C_COMMAND":
                binary = processCommand.processC(line)

            else:
                continue

            out.write(binary + '\n')