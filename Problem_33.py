

for i in range(10, 100):
    for j in range(10, 100):
        if j > i:
            if not (i%10 == 0 and j%10 == 0):
                if str(j)[0] == str(i)[0]:
                    if int(str(j)[1]) != 0:
                        if i/j == int(str(i)[1]) / int(str(j)[1]):
                            print(i, '/', j, 'is', int(str(i)[1]), '/', int(str(j)[1]))
                if str(j)[0] == str(i)[1]:
                    if int(str(j)[1]) != 0:
                        if i / j == int(str(i)[0]) / int(str(j)[1]):
                            print(i, '/', j, 'is', int(str(i)[0]), '/', int(str(j)[1]))
                if str(j)[1] == str(i)[0]:
                    if int(str(j)[0]) != 0:
                        if i / j == int(str(i)[1]) / int(str(j)[0]):
                            print(i, '/', j, 'is', int(str(i)[1]), '/', int(str(j)[0]))
                if str(j)[1] == str(i)[1]:
                    if int(str(j)[0]) != 0:
                        if i / j == int(str(i)[0]) / int(str(j)[0]):
                            print(i, '/', j, 'is', int(str(i)[0]), '/', int(str(j)[0]))

