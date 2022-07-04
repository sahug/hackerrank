#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    # Each Year has 2 cycle/period start with spring(*2) and summer(+1), initial size = 1
    # So we get each year a tree grows by - 1*2 + 1 or 1*c+1
    if n < 3:
        return n + 1
    if n % 2 == 0:
        return (utopianTree(n - 2) * 2) + 1
    else:
        return (utopianTree(n - 2) + 1) * 2        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()