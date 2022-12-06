# Advent of Code 2022 - day 6 --- anthorne

signal = open("day6_input.txt", "r")


def packet_marker(buffer):
    buff = []
    for a in buffer:
        buff.append(a)
    for i in range(len(buff)):
        b = buff.pop()
        for x in buff:
            if x == b:
                return False
    return True


buffer_4 = []
buffer_14 = []
packet_counter = 0
start_of_packet_found = False
start_of_message_found = False
for line in signal:
    for sig in line:
        packet_counter += 1
        buffer_4.append(sig)
        buffer_14.append(sig)
        if not start_of_packet_found:
            if len(buffer_4) >= 4:
                if len(buffer_4) > 4:
                    buffer_4.pop(0)
                if packet_marker(buffer_4):
                    print("This is the start-of-packet: " + str(buffer_4) + " and the packet is: " + str(packet_counter))
                    part_one = packet_counter
                    start_of_packet_found = True
        if not start_of_message_found:
            if len(buffer_14) >= 14:
                if len(buffer_14) > 14:
                    buffer_14.pop(0)
                if packet_marker(buffer_14):
                    print("This is the start-of-message: " + str(buffer_14) + " and the packet is: " + str(packet_counter))
                    part_two = packet_counter
                    start_of_message_found = True


print(" - Part one - How many characters need to be processed before the first start-of-packet marker is detected?")
print("            Answer: " + str(part_one))

print(" - Part two - How many characters need to be processed before the first start-of-message marker is detected?")
print("            Answer: " + str(part_two))
