#!/usr/bin/python
#Problem 39!
#8th May 2008
#For which value of p < 1000, is the number of solutions maximised?
import math
max_count=0
max_p=0
for p in range(1,1000):
	count=0
	for a in range(1,500):
		for b in range(a,500):
			c=p-a-b
			if c>0:
				s=a*a+b*b-c*c
			else:
				break
			if not s:
				count+=1
			if count>max_count:
				max_count=count
				max_p=p
	print p,count
print max_p