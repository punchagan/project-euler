#!/usr/bin/python
#Problem 7!
#What is the 10001st prime number?
import math
number=10001
a=[2]
n=3
while len(a)<number:
	for i in range(0,len(a)):
		if n%a[i]==0:
			prime=0
			break
		else:
			prime=1
	if prime:
		a+=[n]
#		print n, "\t", len(a)
	n+=2

print a[-1]

#Any prime greater than 3 can be written as 6k+/-1. You could make use of that.