#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    size = len(arr)
    
    plus = 0
    minus = 0
    zero = 0
    
    for i in range (size):
        if (arr[i] > 0):
            plus += 1
        elif (arr[i] < 0):
            minus += 1
        else:
            zero += 1
    
    return (plus/size, minus/size, zero/size)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
