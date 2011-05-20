#!/usr/bin/python
#Problem 55!
#8th May 2008
#How many Lychrel numbers are there below ten-thousand?
def reverse(num):
	num_str=str(num)
	rev_str=""
	for i in range(0,len(num_str)):
		rev_str+=num_str[-1-i]
	return int(rev_str)

count=0
for i in range(10,10001):
	run=0
	num=i
	#print i
	while run<51:
		run+=1
		num+=reverse(num)
		if num==reverse(num):
			break
	if run==51 and num!=reverse(num):
		count+=1
print count