import re
data = open('../inputs/day_7').readlines()

ssl_support_count = 0

for line in data:
    bracket = False
    valid_aba_seqs = []
    valid_bab_seqs = []
    for i in range(len(line)-2):
        start = 0 + i
        stop = start + 3
        prev = max(0, start-1)
        slice = line[start:stop]
        if '[' in slice:
            bracket = True
        if ']' is line[prev]:
            bracket = False
        if slice[0] == slice[2] and slice[0] != slice[1] and not '[' in slice and not ']' in slice:
            if bracket:
                valid_bab_seqs.append(slice)
            else:
                valid_aba_seqs.append(slice)

    ssl_support = False
    for aba in valid_aba_seqs:
        inverted = "".join([aba[1], aba[0], aba[1]])
        if inverted in valid_bab_seqs:
            ssl_support = True
            print(inverted, valid_bab_seqs)
        if ssl_support:
            break
    if ssl_support:
        ssl_support_count += 1

print(ssl_support_count)

