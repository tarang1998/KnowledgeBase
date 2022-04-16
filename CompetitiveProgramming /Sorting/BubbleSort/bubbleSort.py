#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    
    totalNoOfSwaps = 0
    
    for i in range(0, len(a)):
        
        swapCount = 0 
        
        for j in range(0, len(a)-1):
            
            if(a[j] > a[j+1]):
                
                swapCount+=1
                totalNoOfSwaps+=1
                
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
          
        #If condition is satisfied the array is already sorted        
        if(swapCount == 0 ):
            break
        
    print("Array is sorted in {0} swaps.".format(totalNoOfSwaps))
    print("First Element:",a[0])
    print("Last Element:",a[len(a)-1])
            
                
                
                
            
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
