#!/bin/usr/env python
from FUF import *
NUM=1000000000
if __name__ == "__main__":
    primes=primeList(100)
    primesInd=[]
    for each in primes:
        primesInd+=[maxPower(NUM,each)]
    print primesInd

