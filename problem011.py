#!/usr/bin/env python

array=open('./docs/problem011.txt')
arr=[]

for row in array:
    row.strip()
    arr+=[row.split()]
for m in range(0,20):
    for n in range(0,20):
        arr[m][n]=int(arr[m][n])


def rowprod(num):
    max=1
    for m in range(0,20):
        for n in range(0,17):
            p=num[m][n]*num[m][n+1]*num[m][n+2]*num[m][n+3]
            if p>=max:
                max=p
    return max

def colprod(num):
    max=1
    for m in range(0,17):
        for n in range(0,20):
            p=num[m][n]*num[m+1][n]*num[m+2][n]*num[m+3][n]
            if p>=max:
                max=p
    return max
        
def diaprod(num):
    max=1
    for m in range(0,17):
        for n in range(0,17):
            p=num[m][n]*num[m+1][n+1]*num[m+2][n+2]*num[m+3][n+3]
            if p>=max:
                max=p
    for m in range(0,17):
        for n in range(3,20):
            p=num[m][n]*num[m+1][n-1]*num[m+2][n-2]*num[m+3][n-3]
            if p>=max:
                max=p

    return max

rowp=rowprod(arr)
colp=colprod(arr)
diap=diaprod(arr)

maxp=rowp
if colp>maxp:
    maxp=colp

if diap>maxp:
    maxp=diap

print maxp
