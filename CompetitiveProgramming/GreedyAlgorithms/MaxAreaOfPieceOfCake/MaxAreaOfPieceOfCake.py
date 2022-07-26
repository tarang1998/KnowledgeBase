# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    
    
    def partition(self,arr,low,high):
        
        pivot = arr[high]
        
        swap_index = low-1
        
        for i in range(low,high):
            
            if(arr[i] < pivot):
                
                swap_index += 1
                
                arr[swap_index],arr[i] = arr[i],arr[swap_index]
        

        swap_index += 1
        arr[swap_index],arr[high] = arr[high],arr[swap_index]

        
        
        return swap_index
            
        
    def quickSort(self,arr,low,high):
        
        if(low<high):
            
            p = self.partition(arr,low,high)
            
            self.quickSort(arr,low,p-1)
            
            self.quickSort(arr,p+1,high)
            
    
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        
        #Sort the horizontal cuts
        self.quickSort(horizontalCuts,0,len(horizontalCuts)-1)
        horizontalCuts.append(h)
        
        #Sort the vertical cuts
        self.quickSort(verticalCuts,0,len(verticalCuts)-1)
        verticalCuts.append(w)
        
        print(horizontalCuts,verticalCuts)
        
        maxHorizontalDifference = horizontalCuts[0]
        
        for i in range(1,len(horizontalCuts)):
            
            if(horizontalCuts[i] - horizontalCuts[i-1] > maxHorizontalDifference):
                
                maxHorizontalDifference = horizontalCuts[i] - horizontalCuts[i-1] 
                
        maxverticalDifference = verticalCuts[0]
        
        for i in range(1,len(verticalCuts)):
            
            if(verticalCuts[i] - verticalCuts[i-1] > maxverticalDifference):
                
                maxverticalDifference = verticalCuts[i] - verticalCuts[i-1] 
                
        print(maxHorizontalDifference,maxverticalDifference)
                
        return (maxHorizontalDifference * maxverticalDifference)%(pow(10,9)+7)
            
            

        
        
        