#!/usr/bin/python
#Problem 53!
#7th May 2008
#How many values of  nCr, for 1 <= n <= 100, are greater than one-million?
count=0
million=1000000
for n in range(23,101,1):
	for r in range(0,n+1):
		com=1
		for p in range(0,r):
			com=com*(n-p)/(p+1)
		print n,r,com
		if com>=million:
			count+=1
print count