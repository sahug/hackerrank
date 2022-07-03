#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    row = len(arr)
    col = len(arr[0])
    right_diagonal = 0
    left_diagonal = 0
    
    for r in range(row):
        left_diagonal  = left_diagonal + arr[r][(col-1)-r]
        for c in range(col):
            if r == c:
                right_diagonal = right_diagonal + arr[r][c]
            
    return abs(right_diagonal -  left_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
