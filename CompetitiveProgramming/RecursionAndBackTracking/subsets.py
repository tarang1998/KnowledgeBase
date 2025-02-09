import copy 

class Solution:

    # Time Complexity : O(2^n)
    # Space Complexity : O(2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(copy.deepcopy(subset))
                return

            ele = nums[i]

            #Include the element
            subset.append(ele)
            dfs(i+1)

            #Do not include the element 
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res
        