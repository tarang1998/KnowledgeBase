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
    

    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mergeSort(0,len(arr)-1,arr)

    print(arr)
