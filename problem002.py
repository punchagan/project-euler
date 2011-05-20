#!/usr/bin/python
#Problem 2!
#Find the sum of all the even-valued terms in the sequence which do not exceed four million
sum=0
a=[1,1]
i=2
while 1:
	a += [a[i-1]+a[i-2]]
	if a[i]%2==0:
		sum=sum+a[i]
	if not a[i]<=4000000:			#implementing a do-while loop!
		break
	i+=1
print sum

#this program doesn't need an array. three variables would have sufficed.
