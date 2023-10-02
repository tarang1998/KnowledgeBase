class Solution:


    # Time Complexity : O(len(nums) * Sum(nums))
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # key : (index,value) value : [-sum(nums), sum(nums)]
        # value : number of possible ways to achieve the target value 
        # after parsing through the entire list given the combination of (index,value)
        dp = {}


        def dfs(index,amount):

            if(index >= len(nums)):
                if(amount == target):
                    return 1
                else:
                    return 0

            if((index,amount) in dp):
                return dp[(index,amount)]
            
            dp[(index,amount)] = dfs(index+1, amount-nums[index]) + dfs(index+1, amount + nums[index])
            return dp[(index,amount)]

            
        return dfs(0,0)

        