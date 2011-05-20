#!/usr/bin/python
#Problem 58!
#8th May 2008
#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
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

total=1
count=1
s=1001
num=1
n=1
ratio=100
side=1

while ratio >=10:
	for i in range(1,5):
		num+=2*n
		total+=1
		if is_prime(num):
			count+=1
	ratio=count*100.0/total
	n+=1
	side+=2
	print ratio,side
print ratio,side