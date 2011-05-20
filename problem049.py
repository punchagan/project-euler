from FUF import primeList

pl = primeList(10000)

words = [str(each) for each in pl]

numdict = {}
for each in words:
    kwrd = list(str(each))
    kwrd.sort()
    kwrd = ''.join(kwrd)
    if kwrd in numdict:
	numdict[kwrd] = numdict[kwrd] + " " + each
    else:
	numdict[kwrd] = each
                                    
for each in numdict.keys():
    if numdict[each].count(" ")<2 or len(each) < 4:
        numdict.pop(each)
    else:
        a = [int(each) for each in numdict[each].split()]
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[j]*2 - a[i] in a:
                    print str(a[i]) + str(a[j]) + str(a[j]*2 - a[i])
