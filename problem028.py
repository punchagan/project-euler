#!/usr/bin/python
#Problem 28!
#8th May 2008
#What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?
sum=1
s=1001
num=1
for n in range(1,(s+1)/2):
	for i in range(1,5):
		num+=2*n
		sum=sum+num
print sum