#!/bin/python3

import sys


def solve(grades):
    # Complete this function
    result = []
    for i in grades:
        if i % 10 > 5:
            if 10 - (i % 10) < 3 and i + (i % 10) >= 40:
                result.append(i + (10 - i % 10))
            else:
                result.append(i)
        else:
            if 5 - (i % 5) < 3 and i + (i % 5) >= 40:
                result.append(i + (5 - i % 5))
            else:
                result.append(i)
    return result


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))