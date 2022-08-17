# https://leetcode.com/problems/binary-trees-with-factors/

class Solution:
    
    def partition(self,array,low,high):
        
        pivot = array[high]
        
        counter = low
        
        swapIndex = low-1 
        
        while(counter < high):
            
            if(array[counter] < pivot):
                swapIndex += 1 
                array[swapIndex],array[counter] = array[counter],array[swapIndex]
                
                
                
            counter +=1
        
        swapIndex += 1 

        array[swapIndex],array[high] = array[high],array[swapIndex]
        
        return swapIndex

                
    
    
    def quickSort(self,array,low,high):
        
        if(low >= high):
            return 
        
        p = self.partition(array,low,high)
        
        self.quickSort(array,low,p-1)
        
        self.quickSort(array,p+1,high)
        
        
    
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
        N = len(arr)
        
        #self.quickSort(arr,0,len(arr)-1)
        arr.sort()
        
        dp = [1] * N
        
        index = {ele : index for index,ele in enumerate(arr)}
        
        for i, ele in enumerate(arr):
            
            for j in range(i):
                
                if(ele % arr[j] == 0 ):
                    rightEle = ele/arr[j]
                    
                    if rightEle in index:
                        
                        dp[i] += dp[j] * dp[index[rightEle]]
                        
        return sum(dp)%1000000007
                        
                
                
        
        
        
        
                

                
                
        
        
        
        