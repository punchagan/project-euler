#!/usr/bin/python
#Problem 6!
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
a=0
b=0
for i in range(0,101):
	a+=i
	b+=i*i
a*=a
print a-b 
