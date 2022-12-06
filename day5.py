# Advent of Code 2022 - day 5 --- anthorne

class Stack:
    def __init__(self, name):
        self.name = name
        self.crates = []

    def push(self, crate):
        self.crates.append(crate)

    def pop(self):
        return self.crates.pop()


def init():
    # Fetch data from puzzle input
    starting_stack = []
    instructions = []
    puzzle_input = open("day5_input.txt", "r")
    for row in puzzle_input:
        if row[0:4] != "move" and row != "\n":
            starting_stack.append(row.strip("\n"))
        else:
            if row != "\n":
                instructions.append(row.strip())
    puzzle_input.close()

    # Get the stack length
    stack_len = int(starting_stack.pop().strip()[-1])

    # Create the starting stack
    stacks = []
    for i in range(stack_len):
        s = Stack(i + 1)
        stacks.append(s)
    for c in range(len(starting_stack)):
        pos = 1
        s = starting_stack.pop()
        for stack in stacks:
            crate = s[pos:pos + 1]
            if crate != " " and crate != "":
                stack.push(crate)
            pos += 4

    show_stacks(stacks)
    return stacks, instructions


def show_stacks(s):
    rows_to_print = []
    rows_len = int(s[-1].name)
    max_cols = 0
    for r in s:
        if len(r.crates) > max_cols:
            max_cols = len(r.crates)
    for col in range(max_cols, 0, -1):
        row = ""
        for r in s:
            if len(r.crates) >= col:
                row += "[" + str(r.crates[col - 1]) + "] "
            else:
                row += "    "
        rows_to_print.append(row)
    row = " "
    for i in range(rows_len):
        row += str(i + 1) + "   "
    row += "\n"
    rows_to_print.append(row)
    for x in rows_to_print:
        print(x)


# - Part one -
print(" - Advent of Code - day 5 - starting position\n")
stacks, instructions = init()

# Execute instructions - CrateMover 9000
for i in instructions:
    print(" >> " + str(i) + "\n")
    num_of_crates_to_move = int(i.split(" ")[1].strip())
    move_from = int(i.split(" ")[3].strip())
    move_to = int(i.split(" ")[5].strip())
    for m in range(num_of_crates_to_move):
        stacks[move_to-1].push(stacks[move_from-1].pop())
        show_stacks(stacks)

# Get the answer for Part One
print(" - Part one - After the rearrangement procedure completes, what crate ends up on top of each stack?")
part_one = ""
for s in stacks:
    part_one += (s.crates[-1])
print("            Answer: " + str(part_one))


# - Part two -
stacks, instructions = init()

# Execute instructions - CrateMover 9001
crate_mover_9001 = []
for i in instructions:
    print(" >> " + str(i) + "\n")
    num_of_crates_to_move = int(i.split(" ")[1].strip())
    move_from = int(i.split(" ")[3].strip())
    move_to = int(i.split(" ")[5].strip())
    for m in range(num_of_crates_to_move):
        crate_mover_9001.append(stacks[move_from-1].pop())
    for n in range(num_of_crates_to_move):
        stacks[move_to-1].push(crate_mover_9001.pop())
        show_stacks(stacks)

# Get the answer for Part Two
print(" - Part two - After the rearrangement procedure completes, what crate ends up on top of each stack?")
part_two = ""
for s in stacks:
    part_two += (s.crates[-1])
print("            Answer: " + str(part_two))

print("\n    Part one        Answer: " + str(part_one))
print("    Part two        Answer: " + str(part_two))