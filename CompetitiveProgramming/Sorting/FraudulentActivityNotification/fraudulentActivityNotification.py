
#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def getTwiceOfMedian(count, d):
    
    #Storing the cummulative sum in the count array 
    for i in range(1,201):
        count[i]+=count[i-1]
        
    

    a= 0
    b= 0
    
    #If d is even
    if(d%2==0):
        first = d//2
        
        second = d//2+1
        
        for i in range(0,201):
            if(first<=count[i]):
                a = i
                break
        
        for i in range(0,201):
            if(second<=count[i]):
                b = i
                break 
            
                
    #If d is odd
    else:
        first = d//2+1
        for i in range(0,201):
            if(first<=count[i]):
                a = 2*i  
                break;      
    
    
    median = a+b
    return median

def activityNotifications(expenditure, d):
    # Write your code here
    
    noOfNotifications = 0
    
    #Array to store count of elements from 0 - 200
    #Given Question Constraint :  
    count = [0]*201
    
    #Finding the occurences of the element from : [0,d]
    for i in range(0,d):
        count[expenditure[i]] += 1
        
        
    for i in range(d,n):
        
        twiceOfMedian = getTwiceOfMedian(count.copy(),d)
        
        if(expenditure[i]>= twiceOfMedian):
            noOfNotifications +=1
            
        #updating the count array
        count[expenditure[i]]+=1
        count[expenditure[i-d]]-=1
        
    return noOfNotifications
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
