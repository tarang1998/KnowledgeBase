#https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1


#User function Template for python3

class Solution:
    

    
    
    def partition(self,low,high,array):
        
        pivot = array[high][1]
        
        swappingIndex = low - 1
        
        for i in range(low,high):
            
            if (array[i][1] <= pivot):
                
                swappingIndex += 1
                
                array[swappingIndex],array[i] = array[i],array[swappingIndex]
                
        swappingIndex += 1
        
        array[swappingIndex],array[high] = array[high],array[swappingIndex]
        
        return swappingIndex
                
                
            
        
        
    
    
    def quickSort(self,low,high,arr):
        
        if(low < high):
            
            p = self.partition(low,high,arr)
            
            self.quickSort(low,p-1,arr)
            
            self.quickSort(p+1,high,arr)
            
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        # Array holds the start, end and position of each meeting 
        meetings = []
        
        for i in range(0,n):
            
            meetings.append([start[i],end[i],i+1])
            
            
        self.quickSort(0,n-1, meetings)
        

        endTime =  meetings[0][1]
        
        totalMeetings = 1 
        
        for i in range(1,n):
            
            if(meetings[i][0] > endTime):
                
                endTime = meetings[i][1]
                totalMeetings += 1
                
        return totalMeetings
            
            
        
        
            
        
    
            
        
        
        

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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends