#!/usr/bin/python
#Problem 037!
#9th May, 2008
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
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
#print is_prime(11)
count=11
sum=0
n=11
x=""
y=""
while count>0:
	yes=1
	#print n
	for a in range(0,len(str(n))):
		x=int(str(n)[a:])
		y=int(str(n)[:len(str(n))-a])
		if is_prime(x) and is_prime(y):
			#print x,y
			continue
		else:
			yes=0
			break
	if yes:
		sum+=n
		print 12-count,n
		count-=1
	if n%6==5:
		n+=2
	else:
		n+=4
print sum