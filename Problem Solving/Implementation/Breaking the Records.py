#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    games = len(scores)
    
    high, low = [scores[0]]*games, [scores[0]]*games

    i, h, l = 0, 0, 0
    
    while i < len(scores) - 1:
        if scores[i+1] > high[i]:
            high[i+1] = scores[i+1]        
            h += 1
        else: high[i+1] =  high[i]
        
        if scores[i+1] < low[i]:            
            low[i+1] = scores[i+1]
            l += 1
        else: low[i+1] = low[i]
        
        i += 1
        
    return [h, l]
        
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
