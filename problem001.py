#!/usr/bin/python
#Yes! Here I go!
# Finding Sum of all multiples of 3 or 5 below 1000
sum=0
i=1
for i in range(1,1000):
	if i%3==0 or i%5==0 :
		sum=sum+i
print sum
