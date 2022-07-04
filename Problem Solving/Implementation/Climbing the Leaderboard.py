#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here                    
    r = set(ranked)
    l = list(r)
    l.sort(reverse=True)
    fr = []
    for i in player:        
        ## Takes Longer
        # l.append(i)
        # l.sort(reverse=True)        
        # fr.append(l.index(i) + 1)
        while l and i >= l[-1]:
            l.pop()
        fr.append(len(l) + 1)        
    return fr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
