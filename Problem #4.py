''' PROMPT
Objective
In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Sample Input 1

24
Sample Output 1

Not Weird
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
        print("Weird")
    elif N in range(2,6):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
