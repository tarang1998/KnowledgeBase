
#https://leetcode.com/problems/combination-sum/


class Solution:
    
    def getUniqueCombinations(self,candidates,position, target , selectedCandidates, results) :
        
        
        if(target == 0):
            results.append(selectedCandidates)
        
        if(candidates[position] > target):
            return 
        
        
            
        
            
        #the element in the position is picked up 
        
        temp = selectedCandidates.copy()
        
        temp.append(candidates[position])
        
        self.getUniqueCombinations(candidates,position,target - candidates[position],temp, results)
        
        #the element in the position is discarded
        
        if(position == len(candidates)-1):
            return
        
        self.getUniqueCombinations(candidates,position+1,target,selectedCandidates.copy(), results)

        
        
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        results = []
        
        self.getUniqueCombinations(candidates,0,target,[],results)
        
        
        return results
        
        
        
        
        
        
        