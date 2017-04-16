import hashlib

data = open('../inputs/day_5').read()
password = ""
i = 0

while len(password) < 8:
    m = hashlib.md5()
    m.update("" + data + str(i))
    digest = m.hexdigest()
    if digest[0:5].count('0') == 5:
        password += digest[5]
        print(digest[0:7])
    i += 1

print(password)

