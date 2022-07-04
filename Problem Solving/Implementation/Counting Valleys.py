#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleycount = level = 0
    
    d = {"U": 1, "D": -1}
    
    for s in path:
        level += d[s]
        print(level, s)
        if level == 0 and s == "U":
            valleycount += 1
    return valleycount    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
