
#https://practice.geeksforgeeks.org/problems/subset-sums2234/1

#User function Template for python3



class Solution:
    
    def calculateSubsetSums(self,index,sum,arr,arrSubsetSums):
        
        if(index == len(arr)-1):
            arrSubsetSums.append(sum)
            return
        
        self.calculateSubsetSums(index+1,sum+arr[index+1],arr,arrSubsetSums)

	    self.calculateSubsetSums(index+1,sum,arr,arrSubsetSums)


    def subsetSums(self, arr, N):
	    
	    arrSubsetSums = []
	    
	    self.calculateSubsetSums(0,0+arr[0],arr,arrSubsetSums)
	    
	    self.calculateSubsetSums(0,0,arr,arrSubsetSums)
	    
	    return arrSubsetSums
	    
	

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")


