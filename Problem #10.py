'''
PROMPT
Objective
Today, we are learning about an algorithmic concept called recursion. Check out the Tutorial tab for learning materials and an instructional video.

Recursive Method for Calculating Factorial
Function Description
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:

int n: an integer
Returns

int: the factorial of
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer,  (the argument to pass to factorial).

Constraints

Your submission must contain a recursive function named factorial.
Sample Input

3
Sample Output

6
'''

#CODE
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
