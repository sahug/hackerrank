#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # We can sort the array first and the sum of first 4 will give is min and last 4 will give max.
    arr.sort()
    max = sum(arr[len(arr)-4:])
    min = sum(arr[:4])
    print(f"{min} {max}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
