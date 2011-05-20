#!/usr/bin/python
#Problem 48!
#8th May 2008
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
sum=0
for a in range(1,1001):
	sum=sum+((a**a)%(10**10))
print sum%(10**10)
