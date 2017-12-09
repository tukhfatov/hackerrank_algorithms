#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

mmin = min(arr)
mmax = max(arr)
totalsum = sum(arr)

print(totalsum-mmax, totalsum-mmin)