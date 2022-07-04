#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    d = dict()
    
    for i in arr:
        d[i] = d.get(i, 0) + 1
    
    d = dict(sorted(d.items(), key=lambda x:x[0], reverse=False))
    s = sorted(d.items(), key=lambda x:x[1], reverse=True)
    
    for i in s:
        return i[0]
        break
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
