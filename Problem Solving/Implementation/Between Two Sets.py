#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    
    def lcm(a, b):
        return (a*b)//math.gcd(a, b)
        
    l = reduce(lcm, a)
    g = reduce(math.gcd, b)
    
    s = 0
    
    print(l, g)
    
    for i in range(l, g+1, l):
        if g % i == 0:
            s+=1
    return s            
    
    # lb = a[-1]
    # ub = b[0]
    # nums = set()
    # fact = set()
        
    # for i in range(lb, ub + lb, lb):
    #     j = 0
    #     while j < len(a):
    #         if i % a[j] == 0:
    #             j += 1
    #         else: break
    #         nums.add(i) 
    
    
    # for i in nums:
    #     j = 0
    #     while j < len(b):
    #         if b[j] % i == 0:
    #             j += 1
    #         else: break
    #         fact.add(i)
        
    # return len(fact)
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
