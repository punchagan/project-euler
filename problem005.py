#!/usr/bin/python
#Problem 5!
#What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
#The Counting Way is DAMN SLOW!
import math
p=1
a=[2]
for n in range(3,21):
	prime=1
	for i in range(0,len(a)):
		if n%a[i] is not 0:
			continue
		else:
			prime=0
			break
	if prime:
		a+=[n]

for n in a:
	power=int(math.log(20,n))
	p=p*math.pow(n,power)

print p