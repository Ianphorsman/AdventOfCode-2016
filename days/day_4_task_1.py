#aoc2016_4a.py
import re
input_file_object = open("../inputs/day_4")
input_as_string = input_file_object.read()
input_file_object.close()


input_separated = input_as_string.split('\n')

input_stripped = []

success = []

numsum = 0

for line in input_separated:
    checksum = line[-6:-1]
    data = line[:-6]
    protoroom = [char for char in data if char.isalpha()]
    protonum = [num for num in data if num in '0123456789']
    idnum = ''.join(protonum)
    room = ''.join((sorted(''.join(protoroom))))
    input_stripped.append((room, checksum, idnum, protoroom))

#########################

for index in range(len(input_stripped)):
    #print("new pair")

    checksum = input_stripped[index][1]
    room = input_stripped[index][0]
    for x in checksum:
        if x not in room:
            #print("invalid - checksum")
            break
    else:
        for y in room:
            if y in checksum:
                continue
            else:
                cs = [room.count(checksum[0]),room.count(checksum[1]),room.count(checksum[2]),room.count(checksum[3]),room.count(checksum[4])]
                if room.count(y) > min(cs):
                    #print("invalid - char count")
                    break
        else:
            success.append(input_stripped[index])



for x in range(len(success)):
    numsum += int(success[x][2])
print(numsum)

##4b

deciphered = []

for i in range(len(success)):
    room = success[i][-1]
    idnum = success[i][2]
    tempstr = ''
    for r in room:
        tempchar = chr(((((ord(r) - 97) + int(idnum)) % 26) + 97))
        tempstr = tempstr+tempchar
        #print(tempstr)
    search = re.search('(northpole)', tempstr)
    if not search == None:
        print(success[i])
    deciphered.append(tempstr)

#print(deciphered)

'''
import re

data = open('../inputs/day_4').readlines()
data = map(lambda line: re.search('(.+)\[(.+)]', line).groups(), data)
real_rooms_sector_sum = 0
real_room = True
for room in data:
    prev_count = 1000
    prev_letter = room[1][0]
    for letter in room[1]:
        letter_count = room[0].count(letter)
        if letter_count > prev_count:
            real_room = False
        elif letter_count == prev_count and letter < prev_letter:
            real_room = False
        prev_count = letter_count
        prev_letter = letter
    if real_room:
        real_rooms_sector_sum += int(re.search('(\d+)', room[0]).group())
        print(room)
    real_room = True

print(real_rooms_sector_sum)

'''