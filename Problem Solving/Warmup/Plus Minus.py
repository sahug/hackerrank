#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size = len(arr)
    neg, pos, zero = 0, 0, 0
    
    for i in arr:
        if i < 0:
            neg = neg + 1
        elif i > 0:
            pos = pos + 1
        elif i == 0:
            zero = zero + 1

    print(format(round(pos/size, 6), ".6f"))            
    print(format(round(neg/size, 6), ".6f"))            
    print(format(round(zero/size, 6), ".6f"))            
            
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
