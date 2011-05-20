#!/usr/bin/python
#Problem 45!
#4th May 2008
#Find the next triangle number that is also pentagonal and hexagonal.
#It can be verified that T285 = P165 = H143 = 40755.

def hexa(num):
	H=num*(2*num-1)
	return H

def penta(num):
	P=num*(3*num-1)/2
	return P

def tri(num):
	T=num*(num-1)/2
	return T

a=285+1
b=165+1
c=143+1
found=0

while not found:
	H=hexa(c)
	P=penta(b)
	T=tri(a)
	while P<H:
		b+=1
		P=penta(b)
		if P==H:
			while T<P:
				a+=1
				T=tri(a)
				if T==P:
					found=1
	c+=1
print H
