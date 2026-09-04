#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # total = 0
    # min_val = arr[0]
    # max_val = arr[0]
    
    # for i in arr:
    #     total += i
        
    #     if i < min_val:
    #         min_val = i
            
    #     if i > max_val:
    #         max_val = i
        
    # a = total - max_val
    # b = total - min_val
        
        
    # print(a,b)            
    print(sum(arr)-max(arr),sum(arr)-min(arr))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
