def is_pan(n):
    compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = int(n)
    product = {}
    upper = int((n**(1/2))//1)+1
    if n in [1, 2]:
        return 0
    else:
        for i in range(2, upper):
            if n % i == 0:
                product.update({i: int(n/i)})
        for i in product:
            pan = []
            for j in str(i):
                pan.append(int(j))
            for j in str(product.get(i)):
                pan.append(int(j))
            for j in str(n):
                pan.append(int(j))
            pan.sort()
            for i in pan:
                try:
                    if int(i) == compare[int(i)-1]:
                        if i == pan[-1]:
                            return 1
                    else:
                        return 0
                    break
                except:
                    return 0
                    break








