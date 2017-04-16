import re
compressed_data = open('../inputs/day_9').read()


def decompress(d):
    bracket = re.search(r'\((\d+)x(\d+)\)', d)
    if not bracket:
        return len(d)
    pos = bracket.start(0)
    sz = int(bracket.group(1))
    rpt = int(bracket.group(2))
    i = pos + len(bracket.group())
    return len(d[:pos]) + decompress(d[i:i+sz]) * rpt + decompress(d[i+sz:])

print(decompress(compressed_data))

