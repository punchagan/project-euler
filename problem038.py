#!/usr/bin/python
#Problem 038!
#9th May 2008
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
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
 
x=""
max_x="1"
for a in range(9999,1,-1):
	x=""
	print a
	for n in range(1,10):
		x+=str(a*n)
		if is_pandigital(int(x),9):
			if int(x)>int(max_x):
				max_x=x
print max_x