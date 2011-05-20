#!/usr/bin/env python
numbers=open('./docs/problem013.txt')
sum=0
for num in numbers:
    num.strip()
    sum+=int(num)

sumstr=str(sum)
print sumstr[0:10]
