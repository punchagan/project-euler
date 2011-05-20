#!/usr/bin/python
#Problem 23!
#8th May 2008
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math
sum=0
def sum_of_div(num):
	sum=-num
	for n in range(1,int(math.floor(math.sqrt(num))+1)):
		if num%n == 0:
			sum+=n
			if n!=num/n:
				sum+=num/n
	
	return sum

abun=[]

for n in range(1,21823):
	if (sum_of_div(n))>n:
		abun+=[n]
print abun

for n in range(1,28124):
	count=1
	for a in abun:
		b=n-a
		if b<=0:
			break
		else:
			if b in abun:
				count=0
				break
			
	if count:
		sum+=n
		print sum
print sum