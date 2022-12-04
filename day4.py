# Advent of Code 2022 - day 4 --- anthorne

assignment_list = open("day4_input.txt", "r")
count_duplicate_assignments = 0
count_overlap = 0


def draw_section_row(section):
    row = ""
    found_first = False
    found_last = False
    for i in range(99):
        if found_first and found_last:
            if i < 10:
                row += "."
            else:
                row += ".."
        if found_first and not found_last:
            if section[1] == i:
                found_last = True
            if i < 10:
                row += " "
            row += str(i)
        if not found_first and not found_last:
            if section[0] == i:
                found_first = True
                if i < 10:
                    row += "."
                row += str(i)
            else:
                row += ".."
    row += " " + str(section)
    print(row)
    return row


def check_duplicate(o1, o2):
    duplicate_order = True
    for s1 in range(o1[0], o1[1] + 1):
        section_found = False
        for s2 in range(o2[0], o2[1] + 1):
            if s1 == s2:
                section_found = True
        if not section_found:
            duplicate_order = False
    return duplicate_order


def check_duplicate_orders(p):
    e1 = p[0]
    e2 = p[1]
    test_1 = check_duplicate(e1, e2)
    test_2 = check_duplicate(e2, e1)
    if test_1 or test_2:
        return True
    else:
        return False


def check_overlap(p):
    e1 = p[0]
    e2 = p[1]
    overlap_found = False
    for s1 in range(e1[0], e1[1] + 1):
        for s2 in range(e2[0], e2[1] + 1):
            if s1 == s2:
                overlap_found = True
    return overlap_found


sections = []
for a in assignment_list:
    elf_pair = [[int(a.split(",")[0].strip().split("-")[0]), int(a.split(",")[0].strip().split("-")[1])],
                [int(a.split(",")[1].strip().split("-")[0]), int(a.split(",")[1].strip().split("-")[1])]]
    sections.append(elf_pair)
    draw_section_row(elf_pair[0])
    draw_section_row(elf_pair[1])
    print(" ")
    if check_duplicate_orders(elf_pair):
        count_duplicate_assignments += 1
    if check_overlap(elf_pair):
        count_overlap += 1

print(" - Part one - In how many assignment pairs does one range fully contain the other?")
print("            Answer: " + str(count_duplicate_assignments) + "\n")

print(" - Part two - In how many assignments pairs do the ranges overlap?")
print("            Answer: " + str(count_overlap))
