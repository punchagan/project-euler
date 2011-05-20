#!/usr/bin/python
#Problem 24!
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
a=[0,1,2,3,4,5,6,7,8,9]
count=0
def fact(n):
	prod=1
	for i in range(n,1,-1):
		prod*=i
	return prod

x=""
index=1000000
while len(a):
	factorial=fact(len(a)-1)
	num=index/factorial
	print num
	index=index%factorial
	print index
	if not index:
		x=x+str(a.pop(num-1))
	else:
		x=x+str(a.pop(num))
print x