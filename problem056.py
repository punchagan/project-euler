#!/usr/bin/python
#Problem 56!
#7th May 2008
#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
max=0
for a in range(1,101):
	for b in range(1,101):
		d_sum=0
		for c in str(a**b):
			d_sum+=int(c)
		print d_sum
		if d_sum>max:
			max=d_sum
print max
