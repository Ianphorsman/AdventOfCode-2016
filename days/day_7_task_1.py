import re
data = open('../inputs/day_7').readlines()

ip_count = 0

for line in data:
    bracket = False
    abba = False
    bracket_abba = False
    for i in range(len(line)-3):
        start = 0 + i
        stop = start + 4
        prev = max(0, start-1)
        slice = line[start:stop]
        if '[' in slice:
            bracket = True
        if ']' is line[prev]:
            bracket = False
        if slice[0] == slice[3] and slice[1] == slice[2] and slice[0] != slice[1]:
            if bracket:
                bracket_abba = True
            else:
                abba = True
        if bracket_abba:
            break
    if abba and not bracket_abba:
        ip_count += 1

print(ip_count)




