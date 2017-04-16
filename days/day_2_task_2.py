input = open('../inputs/day_2').readlines()

keypad = [
    ['Invalid', 'Invalid', 1, 'Invalid', 'Invalid'],
    ['Invalid', 2, 3, 4, 'Invalid', 'Invalid'],
    [5, 6, 7, 8, 9],
    ['Invalid', 'A', 'B', 'C', 'Invalid'],
    ['Invalid', 'Invalid', 'D', 'Invalid', 'Invalid']
]
pos = (2, 0)
keycode = []

for code in input:
    for move in code:
        if move is 'U':
            new_pos = (max(pos[0] - 1, 0), pos[1])
        elif move is 'D':
            new_pos = (min(pos[0] + 1, 4), pos[1])
        elif move is 'L':
            new_pos = (pos[0], max(pos[1] - 1, 0))
        elif move is 'R':
            new_pos = (pos[0], min(pos[1] + 1, 4))

        if keypad[new_pos[0]][new_pos[1]] is not 'Invalid':
                pos = new_pos
    keycode.append(keypad[pos[0]][pos[1]])



print(keycode)
