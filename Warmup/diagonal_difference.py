#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

res1 = 0
res2 = 0
for i in range(n):
    res1 += a[i][i]
    res2 += a[i][n-1-i]

print(abs(res2-res1))