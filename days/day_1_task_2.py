
input = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"

factors = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
)
movement = {
    'R': lambda x: (x + 1) % 4,
    'L': lambda x: (x - 1) % 4
}

direction = 0
location = (0, 0)
memo = set()
repeated_location = False
blocks_away = "Unknown"

for turn in [x.strip() for x in input.split(',')]:
    d, c = turn[0], int(turn[1:])
    direction = movement[d](direction)
    for _ in range(c):
        location = (location[0] + factors[direction][0], location[1] + factors[direction][1])
        if location in memo:
            blocks_away = abs(location[0]) + abs(location[1])
            repeated_location = True
        memo.add(location)
    if repeated_location:
        break


print(blocks_away)
