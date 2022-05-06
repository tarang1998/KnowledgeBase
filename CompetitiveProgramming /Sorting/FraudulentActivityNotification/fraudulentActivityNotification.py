
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

def numberInsertion(arr, start, end, number):
    
    if( start != end ):
            
        for j in range(end, start-1, -1):
            
            if(arr[j] > number):
                
                arr[j+1] = arr[j]
                
            else :
                arr[j+1] = number
                break;
                
                
            
    
def partition(arr,low,high):

    swappingIndex = low - 1
    
    for j in range(low,high):
        
        if(arr[j] <  arr[high]):
            
            swappingIndex+=1
            arr[j], arr[swappingIndex] = arr[swappingIndex], arr[j]
            
    arr[swappingIndex+1], arr[high] = arr[high], arr[swappingIndex+1]
    
    return swappingIndex+1
        
        


def quickSort(arr, low, high):
    
    if(low<high):
        
        p = partition(arr,low,high)
        
        quickSort(arr,low,p-1)
        
        quickSort(arr,p+1, high)
        
    

def calculataMedian(arr):
    
    n = len(arr)
    
    if(n%2 != 0):
        
        return arr[n//2]
    
    else:
        
        return (arr[n//2]+arr[n//2-1])/2

def activityNotifications(expenditure, d):
    # Write your code here
    
    #Using Quick sort to sort the array for the first time  
    quickSort(expenditure, 0,d-1)
    print(expenditure[0:d])
    
    dayExpenditure = expenditure[d]
    
    noOfNotifications = 0 
    
    median = calculataMedian(expenditure[0:d])
    print("Median : {0}".format(median))
    print("DaysExpenditure : {0}".format(expenditure[d]))

    
    if(dayExpenditure>=2*median):
        noOfNotifications+=1
    
    print("Notification : {0}".format(noOfNotifications))

        
    for dayExpenditureIndex in range(d+1,len(expenditure)):
        numberInsertion(expenditure,dayExpenditureIndex-d,dayExpenditureIndex-2,expenditure[dayExpenditureIndex-1])
        print(expenditure[dayExpenditureIndex-d:dayExpenditureIndex])
        median = calculataMedian(expenditure[dayExpenditureIndex-d:dayExpenditureIndex])
        print("Median : {0}".format(median))
        print("DaysExpenditure : {0}".format(expenditure[dayExpenditureIndex]))

        if(expenditure[dayExpenditureIndex]>=2*median):
            noOfNotifications+=1
            
        print("Notification : {0}".format(noOfNotifications))

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
