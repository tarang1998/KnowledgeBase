#https://www.hackerrank.com/challenges/max-array-sum/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
#https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    n = len(arr)
    
   
    if (n == 1):
        
        if (arr[0] < 0):
            return 0 
        
        return arr[0]
    
    maxSubsetMatrix = []
    
    maxSubsetMatrix.append([0,arr[0]])
    
    for i in range(1,n):
        
        sumIfElementNotIncluded = max(maxSubsetMatrix[i-1][0],maxSubsetMatrix[i-1][1])
        
        sumIfElementIncluded = maxSubsetMatrix[i-1][0] + arr[i]
        
        maxSubsetMatrix.append([sumIfElementNotIncluded,sumIfElementIncluded])
    
    return max(maxSubsetMatrix[n-1][0],maxSubsetMatrix[n-1][1])
    
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
