import passes

def assemble(input_file, output_file):
    passes.pass_1(input_file)
    passes.pass_2(input_file, output_file)

# Example usage
assemble('ASMs/Add.asm', 'HACKs/add.hack')
assemble('ASMs/Max.asm', 'HACKs/Max.hack')
assemble('ASMs/MaxL.asm', 'HACKs/MaxL.hack')
assemble('ASMs/Pong.asm', 'HACKs/Pong.hack')
assemble('ASMs/PongL.asm', 'HACKs/PongL.hack')
assemble('ASMs/Rect.asm', 'HACKs/Rect.hack')
assemble('ASMs/RectL.asm', 'HACKs/RectL.hack')
