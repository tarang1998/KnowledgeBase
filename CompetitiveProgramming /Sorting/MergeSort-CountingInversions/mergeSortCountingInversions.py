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
     
    #no of elements in the left sorted array
    n1 = (m-l+1)
    
    #no of elements in the right sorted array
    n2 = (r-m)
    
    
    L = []
    R = []
    
    #Copy the elements of the left sorted array into the temp array : L
    for i in range(0,n1):
        L.append(arr[l+i])
        
    #Copy the elements of the right sorted array into the temp array : R
    for i in range(0,n2):
        R.append(arr[m+1+i])
        
    
    #Merging the two arrays in a sorted manner
    
    i = 0 #Index of the left sorted array
    j = 0 #Index of the right sorted array
    k = l #Index of the merged sub array
    
    inversionCount = 0
    
    while i < n1 and j < n2 :
        
        if(L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
            
        else:
            
            arr[k] = R[j]
            inversionCount += m-j+1
            j += 1
            
        k += 1

            
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

        
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
    print(arr)
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
