#!/bin/python3
#https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    
    counter = [0]*n
    
    for i in range(0, len(queries)):
        a = queries[i][0]
        b = queries[i][1]
        k = queries[i][2]
        
        counter[a-1] += k
        
        if((b+1) <= n):
            counter[b] -= k
            
    maxValue = 0 
    temp = 0
    
    for i in range(0,n):
        temp += counter[i]
        if( temp > maxValue ):
            maxValue = temp
            
    return maxValue
        
                
                                
            
        
        
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
