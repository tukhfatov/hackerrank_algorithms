#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

countPlus = 0
countMinus = 0
countZeros = 0
for i in range(n):
    if (arr[i]>0):
        countPlus += 1
    elif (arr[i] < 0):
        countMinus += 1
    elif (arr[i] == 0):
        countZeros += 1

print('%1.6f'%(countPlus/n))
print('%1.6f'%(countMinus/n))
print('%1.6f'%(countZeros/n))
