from datetime import datetime


initial = datetime.now()


with open('cipher.txt', 'r') as cipher:
    for line in cipher:
        line = line.replace('\n', '')
        chars = line.split(',')

chars = chars[0: 15]
print(chars)
for i in range(len(chars)):
    chars[i] = int(chars[i])


for one in range(97, 123):
    for two in range(97, 123):
        for three in range(97, 123):
            print(chr(one ^ chars[0]), chr(two ^ chars[1]), chr(three ^ chars[2]), chr(one ^ chars[3]), \
                  chr(two ^ chars[4]), chr(three ^ chars[5]), chr(one ^ chars[6]), chr(two ^ chars[7]), \
                  chr(three ^ chars[8]), chr(one ^ chars[9]), chr(two ^ chars[10]), chr(three ^ chars[11]), \
                  chr(one ^ chars[12]), chr(two ^ chars[13]), chr(three ^ chars[14]), )

print(ord('a'))
print(ord('z'))


runTime = datetime.now() - initial


print()
print(runTime)



