class Solution:  
    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # Sorting the items according to the decreasing order of the profit/weight ratio
 
        #self.mergeSortDesc(0,n-1,Items)
        function to sort 
        Items.sort(key = lambda x: x.value/x.weight, reverse = True)
        
        availableCapacity = W
        
        totalValue = 0
        
        for i in range(0,n):
            
            
            if(availableCapacity >= Items[i].weight):
                
                totalValue += Items[i].value
                availableCapacity -= Items[i].weight
                
                if(availableCapacity == 0):
                    
                    break

            elif(availableCapacity > 0):
                
                totalValue +=  (Items[i].value/Items[i].weight) * availableCapacity
                
                break
            
        return totalValue

    def merge(self,low,m,high,arr):
        
        i = low
        
        j = m+1
        
        temp = []
        
        while (i<=m and j <= high):
            
            i_valueWeightRatio = arr[i].value / arr[i].weight
            
            j_valueWeightRatio = arr[j].value / arr[j].weight
            
            if(i_valueWeightRatio > j_valueWeightRatio):
            
                temp.append(arr[i])
                i+=1
            
            else :
                
                temp.append(arr[j])
                j+=1
                
        while (i<=m):
            
            temp.append(arr[i])
            i+=1
            
        while (j<=high):
            
            temp.append(arr[j])
            j+=1
            
        arr[low:high+1] = temp
    
    
    def mergeSortDesc(self,low,high,arr):
        
        if (low < high ):
            
            m = (low + high )//2

            self.mergeSortDesc(low,m,arr)
            
            self.mergeSortDesc(m+1,high,arr)
            
            self.merge(low,m,high,arr)
                
                
                


import atexit
import io
import sys


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

