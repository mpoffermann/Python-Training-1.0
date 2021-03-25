'''
PROMPT
Objective
Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

Example

The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
'''

#CODE
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    result = []
    n = int(input())
    binary = bin(n).replace("0b","",1)
    binary = binary.replace("0",",")
    binary = binary.split(",")
    for i in range(len(binary)):
        result.append(int(binary[i].count("1")))
    final = max(result)
    print(final)
