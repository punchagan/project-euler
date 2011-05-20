#!/usr/bin/python 
#Problem 4!
#Find the largest palindrome made from the product of two 3-digit numbers.
p=0
palpr=0
mpr=0
npr=0
def is_palindrome(x):
	for a in range(0,len(x)/2):
		if int(x[a]) != int(x[len(x)-(1+a)]):
			return 0
		else:
			continue
	return 1

for m in range(999,99,-1):
	for n in range(999,99,-1):
		p=m*n
		if is_palindrome(str(p)):
			if p>palpr:
				palpr=p
				mpr=m
				npr=n
print palpr
print mpr, npr



