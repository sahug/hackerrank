#!/bin/python3

import math
import os
import random
import re
import sys
import operator
import functools

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    sharable = bill.pop(k)
    actual = functools.reduce(operator.add, bill)
    anna_share = round(actual/2)    
    if anna_share == b:
        print("Bon Appetit")
    else: print(b - anna_share)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
