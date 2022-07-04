#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    f = 1
    for i in range(1, n+1):
        f = f*i
    print(f)
        

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
