#!/usr/bin/python
#Problem 92!
#9th May 2008 
#How many starting numbers below ten million will arrive at 89?
count=10000000
arr=[]
for x in range(1,600):
	b=x
	while 1:
		n=0
		for a in str(x):
			n=n+(int(a)*int(a))
		x=n
		if x==89:
			break
		if x==1:
			arr+=[b]
			break
print arr
for x in range(1,10000000):
	n=0
	while x:
		n=n+((x%10)*(x%10))
		x=x/10
	
	if n in arr:
		count-=1
		print count
	
print count