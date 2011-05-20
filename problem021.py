#!/usr/bin/python
#Problem 21!
#4th May 2008
#Evaluate the sum of all the amicable numbers under 10000.
import math
amsum=0

def sum_of_div(num):
	sum=-num
	for n in range(1,int(math.floor(math.sqrt(num))+1)):
		if num%n == 0:
			sum+=n
			if n!=num/n:
				sum+=num/n
	
	return sum

for num in range(1,10001):
	if sum_of_div(sum_of_div(num)) == num:
		if num!=sum_of_div(num) and num<sum_of_div(num):
			amsum+=num
			amsum+=sum_of_div(num)
			print num,sum_of_div(num)
print amsum