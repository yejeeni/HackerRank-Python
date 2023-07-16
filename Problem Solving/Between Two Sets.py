#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# 도움받은 포스팅: https://junho85.pe.kr/1534

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def gcd_list(gcdList):
    gcd_num = 0
    for i in range(len(gcdList)):
        if i == 0:
            gcd_num = gcdList[i]
        else:
            gcd_num = gcd(gcd_num, gcdList[i])
    return gcd_num

def lcm(a, b):
    return a * b / gcd(a, b)
    
def lcm_list(lcmList):
    lcm_num = 0
    for i in range(len(lcmList)):
        if i == 0:
            lcm_num = lcmList[i]
        else:
            lcm_num = lcm(lcm_num, lcmList[i])
    return lcm_num

def getTotalX(a, b):
    lcm = lcm_list(a)
    gcd = gcd_list(b)
    
    count = 1
    lcm_candidate = []
    while(True):
        lcm_mul = lcm * count
        if lcm_mul > gcd:
            break
        lcm_candidate.append(lcm_mul)
        count += 1
        
    result = 0
    for i in lcm_candidate:
        flag = True
        for b_num in b:
            if b_num % i != 0:
                flag = False
        if flag:
            result += 1
            
    return result
    

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
