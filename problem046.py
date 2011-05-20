from FUF import primeList, isPrime, is_perfect_square
pl = primeList(10000)
for i in range(9, 10000, 2):
    if isPrime(i):
        continue
    yes = False
    for j in pl:
        if j > i:
            break
        if is_perfect_square((i-j)/2)[0]:
            yes = True
            break
    if not yes:
        print(i)
    else:
        continue
                                            
