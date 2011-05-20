#!/usr/bin/python
#Problem 10!
#Find the sum of all the primes below two million.
import math
number=2000000
sum=5
n=5
while n<number:
	prime=1
	x=3
	if n%x==0:
		prime=0
	else:
		x=5
		while x<=math.sqrt(n):
			if n%x==0:
				prime=0
				break
			else:
				prime=1
			x=x+2
			
			if n%x==0:
				prime=0
				break
			else:
				prime=1
			x=x+6
				
	if prime and n<number:
		sum+=n
#		print n
	
	prime=1
	x=3
	if (n+2)%x==0:
		prime=0
	else:
		x=5
		while x<=math.sqrt(n+2):
			if (n+2)%x==0:
				prime=0
				break
			else:
				prime=1
			x=x+2
			
			if (n+2)%x==0:
				prime=0
				break
			else:
				prime=1
			x=x+6
				
	if prime and (n+2)<number:
		sum+=(n+2)
#		print n+2
	n+=6

print sum

#Any prime greater than 3 can be written as 6k+/-1. You could make use of that.

#Memory is too slow!!!!!

#!/usr/bin/python
#Problem 10!
#Find the sum of all the primes below two million.
#import math
#number=2000000
#a=[2,3]
#sum=5
#n=5
#while n<number:
#	for i in range(0,len(a)):
#		if a[i]<=math.sqrt(n):
#			if n%a[i]==0:
#				prime=0
#				break
#			else:
#				prime=1
#	if prime and n<number:
#		a+=[n]
#		sum+=n
#		print n
	
#	for i in range(0,len(a)):
#		if a[i]<=math.sqrt(n+2):
#			if (n+2)%a[i]==0:
#				prime=0
#				break
#			else:
#				prime=1
#	if prime and (n+2)<number:
#		a+=[n+2]
#		sum+=(n+2)
#		print n+2
#	n+=6
#
#print sum

#Any prime greater than 3 can be written as 6k+/-1. You could make use of that.
