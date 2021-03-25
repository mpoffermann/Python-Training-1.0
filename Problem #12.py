'''
PROMPT
Objective
Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.

Context
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Example

In the array shown above, the maximum hourglass sum is  for the hourglass in the top left corner.

Input Format

There are  lines of input, where each line contains  space-separated integers that describe the 2D Array .

Constraints

Output Format

Print the maximum hourglass sum in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
'''
#CODE
#!/bin/python3
# Given
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
# my code
s = []
for i in range(4):#range(len(arr)):
    #if i == 4:
    #    break
    #else:
        for x in range(4):#range(len(arr[i])):
            #if x == 4:
            #    break
            #else:
                s.append((sum(arr[i][x:x+3]) + arr[i+1][x+1] + sum(arr[i+2][x:x+3])))
final = max(s)
print(final)
