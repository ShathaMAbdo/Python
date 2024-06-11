def get_primesList(start, end):
    primesList = list()
    if start <= 1:start = 2

    primesNum = [True] * (end + 1)
    for p in range(start, end + 1):
        if (primesNum[p]):
            primesList.append(p)
            for i in range(p, end + 1, p):
                primesNum[i] = False
    return primesList

print(get_primesList(1, 250))
items = get_primesList(1, 250)
file = open('results.txt','w')
for item in items:
	file.write(str(item)+"\n")
file.close()

