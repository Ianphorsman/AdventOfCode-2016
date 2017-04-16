compressed_data = open('../inputs/day_9').read()
decompressed_data = ""

read_index = 0

while read_index < len(compressed_data):
    if compressed_data[read_index] is '(':
        decompress = ""
        for i in range(read_index+1, len(compressed_data)):
            if compressed_data[i] is ')':
                read_index += len(decompress) + 2
                break
            else:
                decompress += compressed_data[i]
        span, repeat = decompress.split('x')

        decompressed_data += compressed_data[read_index:read_index+int(span)] * int(repeat)
        read_index += int(span)
    else:
        decompressed_data += compressed_data[read_index]
        read_index += 1

print(len(decompressed_data))


