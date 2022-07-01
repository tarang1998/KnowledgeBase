
#https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    
    
    #Parameters : (elementIndex,nums,subset, allPossibleSubsetsList)
    def generateSubsets(self, elementPosition, nums , subset,allPossibleSubsetsList ):
                
        if (elementPosition == len(nums)):
            
            if(subset not in allPossibleSubsetsList):
                allPossibleSubsetsList.append(subset)
                
            return
        
        includeElement = subset.copy()
        includeElement.append(nums[elementPosition])
        
        excludeElement = subset.copy()
       
        
        #include the element at position 
        self.generateSubsets(elementPosition+1, nums ,includeElement , allPossibleSubsetsList)
        
        self.generateSubsets(elementPosition+1, nums, excludeElement, allPossibleSubsetsList)
            
        
        
        
        
        
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        allPossibleSubsetsList = []
        nums.sort()
        
        #include the element at position 
        self.generateSubsets(0,nums,[],allPossibleSubsetsList)
        
        #Do not include the element at position
        self.generateSubsets(0,nums,[],allPossibleSubsetsList)

        
        return allPossibleSubsetsList
        
        
        
        
        
        