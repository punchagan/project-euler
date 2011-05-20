#!/usr/bin/python
#Problem 20!
#Find the sum of digits in 100!
factorial=1
sum=0
for i in range(1,101,1):
	factorial*=i

strfac=str(factorial)
for i in range(0,len(strfac)):
	sum+=int(strfac[i])
print sum