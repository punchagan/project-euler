#!/usr/bin/env python
# Problem 201
# July 28th, 2008
# 

#Determine all pythagorean triplets.
count=0
for a in range(1,72):
    for b in range(a,72):
        for c in range(b,101):
            sum=a**2+b**2
            csq=c**2
            if sum==csq:
                print a,b,c
                count+=1
                break
            elif sum<csq:
                break
            else:
                continue
print count
