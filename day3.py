# Advent of Code 2022 - day 3 --- anthorne

sum_of_priorities = 0
rucksacks = open("day3_input.txt", "r")


def get_shared_item(c):
    if len(c) == 2:
        c1 = c[0]
        c2 = c[1]
        for i1 in c1:
            for i2 in c2:
                if i1 == i2:
                    return i1
    if len(c) == 3:
        c1 = c[0]
        c2 = c[1]
        c3 = c[2]
        for i1 in c1:
            for i2 in c2:
                for i3 in c3:
                    if i1 == i2 == i3:
                        return i1


def get_priority_score(item):
    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 1
    for p in priorities:
        if p == item:
            return counter
        counter += 1


for r in rucksacks:
    # Get items in the rucksack compartments
    num_of_items = len(r) - 1
    half_num_items = int(num_of_items / 2)
    compartments = [r[0:half_num_items].strip(), r[half_num_items:].strip()]

    # Get the shared item between the compartments
    shared_item = get_shared_item(compartments)

    # Get the priority score for the shared item
    prio_score = get_priority_score(shared_item)
    sum_of_priorities += prio_score

print(" - Part one - Find the item type that appears in both compartments of each rucksack. "
      "What is the sum of the priorities of those item types?")
print("            Answer: " + str(sum_of_priorities))
rucksacks.close()

# - Part Two -

sum_of_priorities = 0
rucksacks = open("day3_input.txt", "r")

# Arrange the groups
group_member_counter = 1
groups = []
group = []
for r in rucksacks:
    if group_member_counter == 4:
        groups.append(group)
        group_member_counter = 1
        group = []
    group.append(r.strip())
    group_member_counter += 1
groups.append(group)

# Get the priority sum of all the groups
for g in groups:
    shared_item = get_shared_item(g)
    prio_score = get_priority_score(shared_item)
    sum_of_priorities += prio_score

print(" - Part two - Find the item type that corresponds to the badges of each three-Elf group. "
      "What is the sum of the priorities of those item types?")
print("            Answer: " + str(sum_of_priorities))
