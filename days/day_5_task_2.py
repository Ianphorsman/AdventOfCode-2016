import hashlib

data = open('../inputs/day_5').read()
password = [None, None, None, None, None, None, None, None]
i = 0
indexes = ['0', '1', '2', '3', '4', '5', '6', '7']
while None in password:
    m = hashlib.md5()
    m.update("" + data + str(i))
    digest = m.hexdigest()
    if digest[0:5].count('0') == 5:
        if digest[5] in indexes:
            password[int(digest[5])] = digest[6]
            indexes.remove(digest[5])
            print(digest[0:7])
    i += 1

print(''.join(password))

