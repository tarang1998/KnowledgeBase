#hackerrank.com/challenges/luck-balance/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def partition(contests, low, high):
    pivot = contests[high][0]
    
    swappingIndex = low-1
    
    for i in range(low,high):
        
        value = contests[i][0]
        
      
        
        if(value<pivot):
            
            swappingIndex+=1
          
            contests[swappingIndex],contests[i] = contests[i],contests[swappingIndex]
    
    contests[swappingIndex+1],contests[high]= contests[high],contests[swappingIndex+1]
        
    return swappingIndex+1


def quickSort(contests,low,high):
    

    if(low<high):

        p = partition(contests,low,high)
       

        quickSort(contests,low,p-1)
        quickSort(contests,p+1,high)
        

def luckBalance(k, contests):
    # Write your code here
    
    luckBalance = 0
    
    # Sorting of the contest array 
    quickSort(contests,0,len(contests)-1)
    print(contests)
    
    for i in range(len(contests)-1,-1,-1):
        
        luck = contests[i][0]
        importance = contests[i][1]
        
        if(importance == 1):
            if(k>0):
                luckBalance+=luck
                k-=1
            
            else:
                luckBalance-=luck
        
        else:
            luckBalance+=luck
            
    return luckBalance
                
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
