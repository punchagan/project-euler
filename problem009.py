#!/usr/bin/python
#Problem 9!
#3rd May 2008
#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
import math

for a in range(1,500):
	for b in range(a,500):
		c=1000-a-b
		s=a*a+b*b-c*c
		#print s
		if not s:
			print a,b,c
			print a*b*c
			break