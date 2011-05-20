#!/usr/bin/python
#Problem 52!
#6th May 2008
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
found=0
n=1
mul=1
n_sum=0
m_sum=0
while not found:
	found=1
	for i in range(2,7):
		mul=i*n
		for a in str(mul):
			if a not in str(n):
				found=0
				break
		for b in str(n):
			if b not in str(mul):
				found=0
				break
		n_sum=0
		m_sum=0
		for c in str(mul):
			m_sum+=int(c)
		for d in str(n):
			n_sum+=int(d)
		if n_sum!=m_sum:
			found=0
			
		if not found:
			break
	n+=1
	print n

print n-1