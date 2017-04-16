

#input = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"
input = "R8, R4, R4, R8"
input = input.split(', ')

# vectors = [top, right, bottom, left]
vectors = [0, 0, 0, 0]
direction = 0
blocks = []

for movement in input:
    if movement[0] == "R":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    if direction < 2:
        vectors[direction] += int(movement[1:])
    else:
        vectors[direction] -= int(movement[1:])

    blocks.append([vectors[0] + vectors[2], vectors[1] + vectors[3]])

blocks_away = abs(vectors[0] + vectors[2]) + abs(vectors[1] + vectors[3])
print(blocks)

