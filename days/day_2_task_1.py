input = open('../inputs/day_2').readlines()

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
pos = (1, 1)
keycode = []


for code in input:
    for move in code:
        if move is 'U':
            pos = (max(pos[0] - 1, 0), pos[1])
        elif move is 'D':
            pos = (min(pos[0] + 1, 2), pos[1])
        elif move is 'L':
            pos = (pos[0], max(pos[1] - 1, 0))
        elif move is 'R':
            pos = (pos[0], min(pos[1] + 1, 2))
    keycode.append(keypad[pos[0]][pos[1]])

print(keycode)
