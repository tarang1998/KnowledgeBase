#https://www.hackerrank.com/challenges/ctci-merge-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.



#Function to Merge the left and the right sorted arrays
def merge(arr,l,m,r):
    
        
    i = l 
    j = m+1 
    tempArray = []
    
    inversionCount = 0
    
    while i <=m and j <= r :
        
        if(arr[i] > arr[j]):
            # there is an inversion here 
            inversionCount += (m-i+1)
            tempArray.append(arr[j])
            j += 1
            
        else:
            tempArray.append(arr[i])
            i += 1
        
            
            
    # Copy the remaining elements of the first sorted sub array
    while i <= m:
        tempArray.append(arr[i])
        i += 1

 
    # Copy the remaining elements of the second sorted subarray
    while j <= r:
        tempArray.append(arr[j])
        j += 1

    arr[l:r+1] = tempArray
        
    return inversionCount
            
    
        


def mergeSort(arr,l,r):
    
    if(l<r):
    
        m = (l+r)//2
        
        a = mergeSort(arr,l,m)
        
        b = mergeSort(arr,m+1,r)
        
        c = merge(arr,l,m,r)
        
        return (a+b+c)
        
    else:
        return 0;
    
    

def countInversions(arr):
    # Write your code here
    

    inversionCount = mergeSort(arr,0,len(arr)-1)
    return inversionCount
    

    
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
