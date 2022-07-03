#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for r in range(1, n+1):        
        for c in range(n, 0, -1):    
            if c > r:                 
                print(" ", end="")                
            else:
                print("#", end="")
        print("")
            
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
