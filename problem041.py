#!/usr/bin/python
#Problem 041!
#9th May 2008
#What is the largest n-digit pandigital prime that exists?

import math
def is_prime(num):
	n=5
	if num==1:
		return 0
	if num==2 or num==3:
		return 1
	if num%2!=0 and num%3!=0:
		while n<=math.sqrt(num):
			if num%n!=0 and num%(n+2)!=0:
				n+=6
			else:
				return 0
	else:
		return 0
	return 1
			
def is_pandigital(x,n):
	yes=1
	if len(str(x))!=n:
		return 0
	for a in range(1,n+1):
		if str(a) in str(x):
			continue
		else:
			yes=0
			break
	return yes 

#7652413
num=5
max_num=0
while num<987654321:
	n=1+int(math.log10(num))
	#print num,n
	if is_pandigital(num,n):
		print num,max_num
		if is_prime(num):
			if num>max_num:
				max_num=num
			print max_num
			#break
	if num%6==1:
		num+=2
	else:
		num+=4
print max_num
