#!/usr/bin/python
#Problem 035!
#9th May 2008
#How many circular primes are there below one million?
import math
def circulate(x):
	y=""
	y+=x[1:]
	y+=x[0]
	return y

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
			
def is_circ_prime(n):
	p=str(n)
	for a in range(0,len(p)):
		p=circulate(p)
		#print p
		if not is_prime(int(p)):
			return 0
	return 1
	
count=2	#for 2 and 3
n=5

while n<1000000:
	if is_circ_prime(n):
		count+=1
		print n
	if n%6==5:
		n+=2
	else:
		n+=4
print count