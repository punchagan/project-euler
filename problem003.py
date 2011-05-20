#!/usr/bin/python
#Problem 3!
#What is the largest prime factor of the number 600851475143 ?
import math
number=600851475143
a=[2]
pf=[]
prime=0
n=3 
while n<=int(math.sqrt(number)):
	for i in range(0,len(a)):
		if n%a[i]==0:
			prime=0
			break
		else:
			prime=1
	if prime:
		a+=[n]
		if number%n==0:
			pf+=[n]
			number/=n
	n+=2
pf+=[number]
print pf[-1]