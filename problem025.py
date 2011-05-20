#!/usr/bin/python
#Problem 25!
#6th May 2008
#What is the first term in the Fibonacci sequence to contain 1000 digits?
import math
a=1
b=1
c=2
count=2
while math.log10(c)<999:
	c=a+b
	a=b
	b=c
	count+=1
	print count, c
