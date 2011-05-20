from FUF import isPrime, primeList
from pylab import cumsum, find

pl = primeList(5000)
len = 0
max = 0
j = 0
for i in range(2500):
    spl = cumsum(pl[i:])
    spl = spl[spl < 1000000]
    splrev = spl[::-1]

    for item in splrev:
        if isPrime(item):
            pos = find(spl == item)
            if pos > len:
                len = pos
                max = item
                j = i
            break
    print max, len, j
