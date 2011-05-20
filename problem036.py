#!/usr/bin/python
#Problem 034!
#9th May, 2008
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindrome(x):
	for a in range(0,len(x)):
		if x[a] != x[-(1+a)]:
			return 0
		else:
			continue
	return 1

def binarize(x):
	y=""
	while int(x)>0:
		y+=str(int(x)%2)
		x=str(int(x)/2)
	z=""
	for i in range(0,len(y)):
		z+=y[-1-i]
	return z
	
sum=0

for n in range(1,1000000):
	if is_palindrome(str(n)):
		b=binarize(str(n))
		if is_palindrome(b):
			sum+=n
			print n,b
print sum