import re

def part_one(puzzle_input: str) -> str:
    registers, program = puzzle_input.strip().split("\n\n")

    program = [int(n) for n in program.replace("Program: ", "").split(",")]
    register_a, register_b, register_c = [int(n) for n in re.findall(r"^Register [ABC]: (\d+)$", registers, re.MULTILINE)]


    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program) - 1:
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        combo_val = 0
        if operand < 4:
            combo_val = operand
        elif operand == 4:
            combo_val = register_a
        elif operand == 5:
            combo_val = register_b
        elif operand == 6:
            combo_val = register_c
        elif operand == 7:
            pass

        if opcode == 0:
            register_a = register_a // (2 ** combo_val)
            instruction_pointer += 2
        elif opcode == 1:
            register_b = register_b ^ operand
            instruction_pointer += 2
        elif opcode == 2:
            register_b = combo_val % 8
            instruction_pointer += 2
        elif opcode == 3:
            if register_a > 0:
                instruction_pointer = operand
            else:
                instruction_pointer += 2
        elif opcode == 4:
            register_b = register_b ^ register_c
            instruction_pointer += 2
        elif opcode == 5:
            output.append(str(combo_val % 8))
            instruction_pointer += 2
        elif opcode == 6:
            register_b = register_a // (2 ** combo_val)
            instruction_pointer += 2
        elif opcode == 7:
            register_c = register_a // (2 ** combo_val)
            instruction_pointer += 2

    return ",".join(output)

if __name__ == "__main__":
#     puzzle_input = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """

    with open('day17/input.txt') as f:
        puzzle_input = f.read().strip()

    print(f"part one: {part_one(puzzle_input)}") # Answer: 1,4,6,1,6,4,3,0,3
