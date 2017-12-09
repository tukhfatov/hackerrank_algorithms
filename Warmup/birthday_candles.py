#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    tmp = [0] * max(ar)
    for i in range(n):
        tmp[ar[i]-1] += 1
    return max(tmp)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)