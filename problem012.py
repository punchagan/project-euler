#!/usr/bin/python
#Problem 12!
#4th May 2008
#What is the value of the first triangle number to have over five hundred divisors?
import math
def count_div(num):
	count=0
	for n in range(1,int(math.floor(math.sqrt(num)))+1):
		if num%n == 0:
			count+=2 
	return count

div_count=0
a=1
while div_count<5:
	tri_num=a*(a+1)/2
	div_count=count_div(tri_num)
	print tri_num,div_count
	a+=1
print tri_num