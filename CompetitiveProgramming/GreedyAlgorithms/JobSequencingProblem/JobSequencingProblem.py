#https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#


#User function Template for python3

class Solution:
    
    def partition(self,low,high,array):
        
        pivot = array[high].profit
        
        swappingIndex = low - 1

        for i in range(low,high):
            
            if(array[i].profit > pivot):
                
                swappingIndex += 1
                
                array[swappingIndex],array[i] = array[i],array[swappingIndex]
                
        swappingIndex += 1 
        
        array[swappingIndex],array[high] = array[high],array[swappingIndex]
        
        return swappingIndex
            
            
                
    
    def quickSortDesc(self,low,high,arr):
        
        if(low < high):
            
            p = self.partition(low,high,arr)
            
            self.quickSortDesc(low,p-1,arr)
            
            self.quickSortDesc(p+1,high,arr)
            
        
        
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        #self.quickSortDesc(0,n-1,Jobs)
        
        Jobs.sort(key = lambda x: x.profit, reverse = True )
        
        maxDeadLine = 0 
        
        for i in range(0,n):
            
            if(Jobs[i].deadline > maxDeadLine):
                
                maxDeadLine = Jobs[i].deadline

        time = [-1 for i in range(maxDeadLine)]


        jobCount = 0 
        totalProfit = 0
        
        for i in range(0,n):
            
            deadline = Jobs[i].deadline
            

            for j in range(deadline-1,-1,-1):
                
                if(time[j] == -1):
                
                    time[j] = i
                    jobCount += 1
                    totalProfit += Jobs[i].profit
                    break;
                    
        
        
        
                
                
        return [jobCount,totalProfit]

        


        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends