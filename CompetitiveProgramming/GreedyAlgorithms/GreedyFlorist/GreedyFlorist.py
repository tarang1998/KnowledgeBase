#https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms


#!/bin/python3

import math
import os
import random
import re
import sys


def merge(low,m,high,arr):
    
    i = low
    
    j = m+1
    
    temp = []
    
    while (i<=m and j<=high):
        
        if(arr[i]<arr[j]):
            temp.append(arr[i])
            i+=1
            
        else:
            temp.append(arr[j])
            j+=1
            
    while (i<=m):
        temp.append(arr[i])
        i+=1
        
    while (j<=high):
        temp.append(arr[j])
        j+=1
        
    arr[low:high+1] = temp
    
    return

def mergeSort(low,high,arr):
    
    if(low<high):
        
        m = (low + high) // 2
        
        mergeSort(low,m,arr)
        
        mergeSort(m+1, high,arr)
        
        merge(low,m,high,arr)
    
    
# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    
    #sort the given array 
    mergeSort(0,len(c)-1,c)
        
    totalCost = 0 
    
    temp = k 
    previousFlowerCount = 0 
    
    for i in range(len(c)-1,-1,-1):
        
        totalCost += (previousFlowerCount + 1) * c[i]
        
        temp -=1

        
        if(temp == 0):

            temp = k
            
            previousFlowerCount += 1
            

                        
    return totalCost
            
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
