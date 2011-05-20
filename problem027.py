#!/usr/bin/python
#Problem 027!
#8th May 2008
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
import math
def is_prime(num):
	n=5
	if num==1:
		return 0
	if num==2 or num==3:
		return 1
	if num%2!=0 and num%3!=0:
		while n<=math.sqrt(num):
			if num%n!=0 and num%(n+2)!=0:
				n+=6
			else:
				return 0
	else:
		return 0
	return 1
max_count=0
max_prod=0
for a in range(-1000,1000):
	for b in range(-1000,1000):
		n=0
		prime=1
		sol=0
		count=0
		while prime:
			sol=n*n+a*n+b
			if sol>0:
				prime = is_prime(sol)
			else:
				prime=0
			count+=1
			n+=1
		if count>max_count:
			max_count=count
			max_prod=a*b
		print count, a, b
print max_prod, max_count