import heapq

class Solution:
    
    #DP from bottum to top
    def maxResultDownToUp(self, nums, k):
        
        n = len(nums)
        
        #stores the max value from the ith index to n-1
        subSolutions = n * [0]
        
        #The last index has to be included
        subSolutions[n-1] = nums[n-1]
        
        #Max Heap to store (subSolution(i),i)
        heap = []
        
        #Multiplying the cost by -1 in order to create a max heap using heapq
        heapq.heappush(heap,(-subSolutions[n-1], n-1))
        
        for i in range(n-2, -1 , -1):
            
            #keep popping the elements that are out of our window of size k 
            #to find the first element within range
            while(len(heap) and heap[0][1] > i+k):
                heapq.heappop(heap)
            
            subSolutions[i] = -(heap[0][0]) + nums[i]
            
            heapq.heappush(heap,(-subSolutions[i],i))
            
        return subSolutions[0]
    
    #DP from top to bottom
    def maxResult(self,nums,k):
        
        n = len(nums)
        
        subSolutions = []
        
        subSolutions.append(nums[0])
        
        heap = []
        
        heapq.heappush(heap,(-subSolutions[0],0))
        
        for i in range(1,n):
            
            while(heap[0][1] < i-k):
                heapq.heappop(heap)
                
            subSolutions.append(-(heap[0][0]) + nums[i])
            heapq.heappush(heap,(-subSolutions[i],i))
            
        return subSolutions[n-1]
        
                
                
        
        
        
        
        
        

        
        
        
       
                
            
            
            
            
            
        
        
        