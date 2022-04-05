#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


#!/bin/python3

import math
import os
import random
import re
import sys


#With reduced space complexity
#To be worked upon
def minimumSwapsAlternative(arr):
    
    #arr = [4,3,2,1]
    
    swaps = 0;
    
    getIndexOfValue = dict(zip(arr,range(1,len(arr)+1)))
    #{4:1,3:2,2:3,1:4}
    
    for value in range(1,len(arr)+1):
        #value  : 1 
        
        indexOfValue = getIndexOfValue[value]
        #indexOfValue : 4
        
        if(value != indexOfValue):
        #true (1 != 4 )
        
        #after 1st iteration : [1,3,2,4]
            
            valueAtIndex = arr[value-1]
            #valueAtIndex = 4
            
            arr[indexOfValue-1] = valueAtIndex
            getIndexOfValue[valueAtIndex] =  indexOfValue
            swaps += 1
    
    return swaps
        

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #arr = [4,1,3,2]
    getValueAtIndex = dict(enumerate(arr,1)) 
    #{1:4,2:1,3:2,2:4}
    
    getIndexOfValue = {v:k for k,v in getValueAtIndex.items()}
    #{4:1,1:2,3:3,2:4}
    
    noOfSwaps = 0
    
    for index in getValueAtIndex:
        #index = 1
        
        #getting the value stored at index 1 in the array
        valueAtIndex = getValueAtIndex[index]
        #valueAtIndex = 4
        
        
        if(index != valueAtIndex):
            #true (1 != 4)
            
            #get where 1 is stored in the array 
            indexOfValue = getIndexOfValue[index]
            #indexOfValue = 2 
            
            #assigning value = 4 at index = 2 
            getValueAtIndex[indexOfValue] = valueAtIndex
            
            #assigning index = 2 at value 4 
            getIndexOfValue[valueAtIndex] = indexOfValue
            
            #after operation
            #arr = [1,4,3,2]
            
            noOfSwaps += 1
            
    return noOfSwaps
            
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
