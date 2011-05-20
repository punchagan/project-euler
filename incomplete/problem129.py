#!/usr/bin/python
#Problem 129!
#9th May 2008
#Find the least value of n for which A(n) first exceeds one-million

n=2
x=""
lengths=[]
l=1
for a in range(0,1000000):
	x+="1"

while len(x)<10000:
	n+=1
	x="1"
	if n%2!=0 and n%5!=0:
		while int(x)%n!=0:
			x+="1"
		lengths+=[len(x)]
		#print lengths
		#l*=len(x)
		print len(x)
	
print n
			