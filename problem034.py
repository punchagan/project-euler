#!/usr/bin/python
#Problem 34!
#9th May 2008
##Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def fact(n):
	prod=1
	for i in range(n,1,-1):
		prod*=i
	return prod

n=10
sum=0
while n<9*fact(9):
	fac_sum=0
	for a in str(n):
		fac_sum+=fact(int(a))
	if fac_sum==n:
		sum+=n
	n+=1
	print sum