#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    if s[-2:] == "PM" and int(s[:2])!=12:
        return str((12+int(s[:2])))+s[2:-2]
    if s[-2:] == "AM" and int(s[:2])==12:
        return "00"+s[2:-2]
    return s[:-2]

s = input().strip()
result = timeConversion(s)
print(result)
