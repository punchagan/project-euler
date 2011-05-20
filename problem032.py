#!/usr/bin/python
#Problem 032!
#9th May 2008
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
def is_pandigital(x,n):
	yes=1
	if len(str(x))!= n:
		return 0
	for a in range(1,n+1):
		if str(a) in str(x):
			continue
		else:
			yes=0
			break
	return yes 

	
s=[]

for a in range(1,100):
	for b in range(a,2000):
		x=""
		c=a*b
		x+=str(a)+str(b)+str(c)
		#print x
		if is_pandigital(int(x),9):
			if c not in s:
				s+=[c]
			print a,"x",b,"=",c
print sum(s)
