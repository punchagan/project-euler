#!/usr/bin/python
#Problem 14!
#4th May 2008
#Which starting number, under one million, produces the longest chain?
n_max=2
ch_max=1
n=2
while n<1000000:
	m=n
	count=1
	while m!=1:
		if m%2==0:
			m=m/2
			count+=1
		else:
			m=3*m+1
			count+=1
	if count>ch_max:
		n_max=n
		ch_max=count
	n+=1
print n_max
