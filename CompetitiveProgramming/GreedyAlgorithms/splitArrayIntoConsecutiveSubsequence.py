#https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    
    def isPossible(self, nums: List[int]) -> bool:
        
        numCount = {}
        
        for ele in nums :
            
            if ele in numCount:
                numCount[ele] += 1
            else:
                numCount[ele] = 1
                
        subsequence = {}
                
        #Try Placing the number in a subsequence 
        #If it cant be placed in any subsequence create a new one
        #If neither of the condition can be satisfied the number does not belong to any subsequence
        #return False
        
        for i in range(len(nums)):
            
            ele = nums[i]
            

            
            if(numCount[ele] == 0 ):
                continue
            
            
            
            #Check if the number can be a part of a subsequence
            if ele in subsequence and subsequence[ele] != 0 :
                
                subsequence[ele] -=1
                numCount[ele] -= 1
                                
                if (ele+1) in subsequence:
                    subsequence[(ele+1)] += 1
                else:
                    subsequence[(ele+1)] = 1
                    
            #If no. not a part of a subsequence 
            #Try forming a new sequence
            elif(ele+1 in numCount and ele+2 in numCount and numCount[ele+1] != 0 and numCount[ele+2]!=0):
                
                numCount[ele]-=1
                numCount[ele+1]-=1
                numCount[ele+2]-=1
                
                if (ele+3) in subsequence:
                    subsequence[(ele+3)] += 1
                else:
                    subsequence[(ele+3)] = 1             
                    
            else:
                return False
            
        return True
                
                
                
       
                
                
         
        