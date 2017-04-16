data = open('../inputs/day_3').readlines()

real_triangles = sum(
    sides[0] + sides[1] > sides[2]
    for sides in [
        sorted([int(triangle) for triangle in line.split()])
        for line in data
    ]
)

print(real_triangles)