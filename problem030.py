#!/usr/bin/python
#Problem 30!
#6th May 2008
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import math
sum=0
for i in range(32,300000,1):
	str(i)
	sum_dig=0
	for a in str(i):
		sum_dig+=math.pow(int(a),5)
	if sum_dig==i:
		sum+=sum_dig
print sum