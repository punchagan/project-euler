#!/bin/usr/env python
#January 14, 2009
#Frequently Used Functions!


def is_perfect_square(n):
    i = 1
    while i*i < n:
        i += 1
    return i*i == n, i

def isPrime(n):
    """Checks if integer argument is Prime"""
    for i in range(2,is_perfect_square(n)[1]+1):
        if not n%i:
            return False
    return True

def primeList(n):
    """Returns a List of Primes strictly below an integer"""
    plist=[2,3]
    i=5
    for i in range(5, n+1, 6):
        if isPrime(i):
            plist += [i]
        if isPrime(i+2):
            plist += [i+2]
    return plist


def maxPower(a,b):
    """Returns maximum index to which the second argument may be raised, before it exceeds a"""
    i=0
    p=b
    while p<a:
        p*=b
        i+=1
    return i
