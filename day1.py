# Advent of Code 2022 - day 1 --- anthorne

calories_input = open("day1_input.txt", "r")
elves = list()
elf = 0

# Get total calories per elf
for row in calories_input:
    if row.strip() == "":
        elves.append(elf)
        elf = 0
    else:
        elf += int(row.strip())

# Get elf and max value
max_value = 0
for cal in elves:
    if cal > max_value:
        max_value = cal

print(" - Part one - Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?")
print("              Answer: " + str(max_value) + "\n")

# - Part two -
elves.sort(reverse=True)
top_three = elves[0] + elves[1] + elves[2]

print(" - Part two - Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?")
print("              Answer: " + str(top_three) + "\n")
