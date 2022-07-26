#https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

#User function Template for python3

class Solution:    
    
    def merge(self,low,m,high,arr):
        
        temp = []
        
        i = low
        
        j = m+1
        
        while ( i <= m and j <= high ):
            
            if (arr[i][0] <= arr[j][0] ):
                
                temp.append(arr[i])
                i+=1
                
            else:
                
                temp.append(arr[j])
                j+=1
                
        while (i <= m):
        
            temp.append(arr[i])
            i+=1
            
        while (j<= high):
        
            temp.append(arr[j])
            j+=1
            
        arr[low:high+1] = temp
        
        
        
    
    
    def mergeSort(self,low,high,arr):
        
        if (low < high):
            
            m = (low+high)//2
            
            self.mergeSort(low,m,arr)
            
            self.mergeSort(m+1,high,arr)
            
            self.merge(low,m,high,arr)
            
            

            
            
        
    
    
    
    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.

    def minimumPlatform(self,n,arr,dep):
        # code here
        
        trainTimeTable = []
        
        for i in range(0,n):
            
            trainTimeTable.append([arr[i],dep[i]])
            
        self.mergeSort(0,n-1,trainTimeTable)
        
        
        platformInfo = []
        
        platformInfo.append(trainTimeTable[0][1])
        
        for i in range(1,n):
            
            isPlatformAvailable = False 
            
            for j in range(0,len(platformInfo)):
            
                if( platformInfo[j] < trainTimeTable[i][0] ):
                    
                    isPlatformAvailable = True 
                    platformInfo[j] = trainTimeTable[i][1]
                    break
            
            if(isPlatformAvailable == False):
                
                platformInfo.append(trainTimeTable[i][1])
                
        return len(platformInfo)
            
                
        
        
        

        
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends