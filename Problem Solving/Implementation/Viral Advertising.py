#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    # Pattern initial share(s) = 5, like(l) = s/2
    # Each next day, s = l*3 and l=s/2
    
    s = 5
    l = int(s/2)
    t = l
    for i in range(n-1):
        s = l*3
        l = int(s/2)
        t = t+l
    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
